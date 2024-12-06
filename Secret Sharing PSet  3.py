import random

def mod_inverse(a, p):
    """Compute the modular inverse of a modulo p."""
    return pow(a, -1, p)

def evaluate_polynomial(coeffs, x, p):
    """Evaluate a polynomial at a given x modulo p."""
    return sum([coeff * (x ** idx) for idx, coeff in enumerate(coeffs)]) % p

def lagrange_interpolation(shares, p):
    """Reconstruct the secret using Lagrange interpolation."""
    secret = 0
    k = len(shares)
    for j in range(k):
        xj, yj = shares[j]
        numerator = 1
        denominator = 1
        for m in range(k):
            if m != j:
                xm, _ = shares[m]
                numerator = (numerator * (-xm)) % p
                denominator = (denominator * (xj - xm)) % p
        lagrange_coeff = numerator * mod_inverse(denominator, p)
        secret = (secret + yj * lagrange_coeff) % p
    return secret

class ShamirSecretSharing:
    def __init__(self, secret, k, n, p):
        """
        Initialize the Shamir Secret Sharing scheme.
        :param secret: The secret to be shared.
        :param k: Threshold number of shares needed to reconstruct the secret.
        :param n: Total number of shares to generate.
        :param p: A prime number greater than max(secret, n).
        """
        if p <= max(secret, n):
            raise ValueError("Prime p must be greater than the secret and the number of shares.")
        self.secret = secret
        self.k = k
        self.n = n
        self.p = p
        self.coeffs = self.generate_polynomial()

    def generate_polynomial(self):
        """Generate a random polynomial with the secret as the constant term."""
        coeffs = [self.secret]
        for _ in range(1, self.k):
            coeffs.append(random.randint(0, self.p - 1))
        return coeffs

    def split_secret(self):
        """Split the secret into n shares."""
        shares = []
        for i in range(1, self.n + 1):
            y = evaluate_polynomial(self.coeffs, i, self.p)
            shares.append((i, y))
        return shares

    @staticmethod
    def reconstruct_secret(shares, p):
        """Reconstruct the secret from k shares."""
        return lagrange_interpolation(shares, p)

def add_shares(share1, share2, p):
    """Add two shares with the same x-coordinate."""
    if share1[0] != share2[0]:
        raise ValueError("Shares must have the same x-coordinate to be added.")
    return (share1[0], (share1[1] + share2[1]) % p)

def add_public_to_share(share, c, p):
    """Add a public constant to a share."""
    return (share[0], (share[1] + c) % p)

def multiply_share(share, c, p):
    """Multiply a share by a public constant."""
    return (share[0], (share[1] * c) % p)

def multiply_shares(share1, share2, p):
    """Multiply two shares."""
    if share1[0] != share2[0]:
        raise ValueError("Shares must have the same x-coordinate to be multiplied.")
    return (share1[0], (share1[1] * share2[1]) % p)

def generate_beaver_triple(p):
    """Generate a Beaver Triple (a, b, c) where c = a * b mod p."""
    a = random.randint(0, p - 1)
    b = random.randint(0, p - 1)
    c = (a * b) % p
    return ((1, a), (1, b), (1, c))

def multiply_shares_with_beaver(share1, share2, beaver_triple, p):
    """Multiply two shares using a Beaver Triple."""
    a = beaver_triple[0][1]
    b = beaver_triple[1][1]
    c = beaver_triple[2][1]
    d = (share1[1] - a) % p
    e = (share2[1] - b) % p
    product = (c + d * b + e * a + d * e) % p
    return (share1[0], product)

def main():
    # Parameters
    secret = 1234
    k = 3  # Threshold
    n = 5  # Total shares
    prime = 7919  # A prime number greater than max(secret, n)

    # Initialize Shamir Secret Sharing
    sss = ShamirSecretSharing(secret, k, n, prime)

    # Split the secret into shares
    shares = sss.split_secret()
    print("Generated Shares:")
    for share in shares:
        print(f"Share {share[0]}: {share[1]}")
    print()

    # Reconstruct the secret from any k shares
    subset = shares[:k]
    reconstructed = ShamirSecretSharing.reconstruct_secret(subset, prime)
    print(f"Reconstructed Secret from shares {[s[0] for s in subset]}: {reconstructed}\n")

    # Add two shares
    share_sum = add_shares(shares[0], shares[1], prime)
    print(f"Sum of Share 1 and Share 2: {share_sum}")

    # Add a public value to a share
    public_value = 100
    share_plus_public = add_public_to_share(shares[0], public_value, prime)
    print(f"Share 1 + Public Value ({public_value}): {share_plus_public}")

    # Multiply a share by a public value
    multiplier = 5
    share_times_public = multiply_share(shares[0], multiplier, prime)
    print(f"Share 1 * Multiplier ({multiplier}): {share_times_public}\n")

    # Multiply two shares
    share_product = multiply_shares(shares[0], shares[1], prime)
    print(f"Product of Share 1 and Share 2: {share_product}")

    # Generate Beaver Triple
    beaver_triple = generate_beaver_triple(prime)
    print("\nGenerated Beaver Triple:")
    print(f"a: {beaver_triple[0][1]}, b: {beaver_triple[1][1]}, c: {beaver_triple[2][1]}")

    # Multiply shares using Beaver Triple
    beaver_product = multiply_shares_with_beaver(shares[0], shares[1], beaver_triple, prime)
    print(f"Product of Share 1 and Share 2 using Beaver Triple: {beaver_product}")

if __name__ == "__main__":
    main()
