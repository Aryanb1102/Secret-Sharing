# Secret-Sharing

Overview
--------

This Python script implements the **Shamir's Secret Sharing** scheme, a cryptographic protocol for securely splitting a secret into multiple shares and reconstructing the original secret from a subset of those shares. It also includes functionality for performing arithmetic operations on shares, such as addition and multiplication with public values.

Features
--------

*   **Secret Splitting**: Divide a secret into n shares with a threshold of k shares required for reconstruction.
    
*   **Secret Reconstruction**: Reconstruct the original secret from any k shares using Lagrange interpolation.
    
*   **Share Operations**:
    
    *   **Addition of Shares**: Add two shares with the same x-coordinate.
        
    *   **Addition with Public Value**: Add a public constant to a share.
        
    *   **Multiplication with Public Value**: Multiply a share by a public constant.
        
    *   **Multiplication of Two Shares**: Multiply two shares while maintaining the properties of the secret sharing scheme.
        
    *   **Beaver Triples**: Securely multiply shares using pre-shared triples.
        

Requirements
------------

*   Python 3.x
    

Installation
------------

1.  bashCopy codegit clone https://github.com/yourusername/shamir-secret-sharing.gitcd shamir-secret-sharing
    
2.  Verify that Python 3 is installed on your system:bashCopy codepython3 --versionIf not installed, download it from the [official website](https://www.python.org/downloads/).
    

Usage
-----

1.  Execute the Python script using the command line:bashCopy codepython3 shamir\_secret\_sharing.py
    
2.  The script performs the following actions:
    
    *   **Generates Shares**: Splits the secret into n shares.
        
    *   **Reconstructs the Secret**: Reconstructs the secret from the first k shares.
        
    *   **Performs Share Operations**: Demonstrates addition and multiplication operations on the shares.
        
    *   **Uses Beaver Triples**: Demonstrates secure multiplication of shares using Beaver Triples.
        

_Note_: The actual share values will vary with each run due to the random generation of polynomial coefficients and Beaver Triples.

Code Structure
--------------

*   **Helper Functions**:
    
    *   mod\_inverse(a, p): Computes the modular inverse of a modulo p.
        
    *   evaluate\_polynomial(coeffs, x, p): Evaluates a polynomial at a given x modulo p.
        
    *   lagrange\_interpolation(shares, p): Reconstructs the secret from shares using Lagrange interpolation.
        
*   **ShamirSecretSharing Class**:
    
    *   **Initialization**: Sets up the secret, threshold k, total shares n, and prime p.
        
    *   generate\_polynomial(): Generates a random polynomial with the secret as the constant term.
        
    *   split\_secret(): Generates n shares by evaluating the polynomial at distinct x values.
        
    *   reconstruct\_secret(shares, p): Reconstructs the secret from a subset of shares.
        
*   **Share Operations**:
    
    *   add\_shares(share1, share2, p): Adds two shares with the same x-coordinate.
        
    *   add\_public\_to\_share(share, c, p): Adds a public constant to a share.
        
    *   multiply\_share(share, c, p): Multiplies a share by a public constant.
        
    *   multiply\_shares(share1, share2, p): Multiplies two shares.
        
    *   generate\_beaver\_triple(p): Generates a Beaver Triple (a, b, c) where c = a \* b mod p.
        
    *   multiply\_shares\_with\_beaver(share1, share2, beaver\_triple, p): Uses Beaver Triple to securely multiply two shares.
        
*   **Main Function**:
    
    *   Demonstrates splitting and reconstruction of the secret.
        
    *   Performs arithmetic operations on the shares.
        
    *   Demonstrates multiplication of shares using Beaver Triples.
        

Important Considerations
------------------------

*   **Security**:
    
    *   Ensure that the prime p is sufficiently large to prevent brute-force attacks.
        
    *   Use cryptographically secure random number generation.
        
    *   In real-world applications, implement Beaver Triples and other secure multiparty computation protocols with proper safeguards.
        
*   **Multiplying Shares**:
    
    *   Multiplying shares increases the degree of the polynomial, requiring additional handling to maintain the threshold property.
        

License
-------

This project is licensed under the [MIT License](LICENSE).

Acknowledgements
----------------

*   Shamir, Adi. "How to share a secret." _Communications of the ACM_ 22.11 (1979): 612-614.
