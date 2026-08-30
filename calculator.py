#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Multiplicateur Type Sans Zéro
Revolutionary arithmetic system without the digit "0"
"""

def contains_zero(n):
    """Check if number contains digit 0"""
    return '0' in str(n)

def find_next_without_zero(n):
    """Find the next number without digit 0"""
    while contains_zero(n):
        n += 1
    return n

def multiply_without_zero(a, b):
    """
    Multiply two numbers in the zero-free system
    
    Algorithm:
    1. Multiply normally (classic)
    2. If result contains 0, find next number without 0
    3. Return the result
    """
    classic_result = a * b
    
    # If contains zero, find next number without zero
    if contains_zero(classic_result):
        result = find_next_without_zero(classic_result)
    else:
        result = classic_result
    
    return result

def divide_without_zero(dividend, divisor):
    """
    Divide in the zero-free system
    Uses the inverse of multiplication
    """
    if divisor == 0:
        return None
    
    result = dividend / divisor
    return result

def format_number(n):
    """Format number for display"""
    return f"{n:,}".replace(',', ' ')

def main():
    """Main calculator loop"""
    print("\n" + "="*60)
    print("--- CALCULATRICE DOUBLE SYSTÈME : MULTIPLICATION & REVERSE ---")
    print("Tapez 'quitter' pour arrêter.")
    print("="*60 + "\n")
    
    while True:
        try:
            # Get first number
            user_input_a = input("Premier nombre : ").strip()
            if user_input_a.lower() == 'quitter':
                print("\nAu revoir!")
                break
            
            a = int(user_input_a)
            
            # Get second number
            user_input_b = input("Deuxième nombre : ").strip()
            if user_input_b.lower() == 'quitter':
                print("\nAu revoir!")
                break
            
            b = int(user_input_b)
            
            # Check if either number contains zero
            if contains_zero(a) or contains_zero(b):
                print("-> Pas de réponse (le chiffre 0 est interdit dans votre logique.)\n")
                continue
            
            print("\n" + "="*60)
            
            # MULTIPLICATION
            print(" L'OPÉRATION MULTIPLE (Votre produit) :")
            our_result = multiply_without_zero(a, b)
            classic_result = a * b
            
            print(f"[*] VOTRE RÉPONSE : {a} x {b} = {our_result}")
            print(f"[-] RÉPONSE CLASSIQUE : {a} x {b} = {classic_result}")
            
            # DIVISION INVERSE
            print("\n L'OPÉRATION INVERSE (Le montant divisé par le multiple) :")
            our_division = divide_without_zero(our_result, b)
            classic_division = divide_without_zero(classic_result, b)
            
            # Format division results
            if our_division == int(our_division):
                our_division_str = str(int(our_division))
            else:
                our_division_str = str(our_division)
            
            if classic_division == int(classic_division):
                classic_division_str = str(int(classic_division)) + ".0"
            else:
                classic_division_str = str(classic_division)
            
            print(f"[*] VOTRE RÉPONSE : {our_result} / {b} = {our_division_str}")
            print(f"[-] RÉPONSE CLASSIQUE : {classic_result} / {b} = {classic_division_str}")
            
            print("="*60 + "\n")
            
        except ValueError:
            print("-> Erreur : Veuillez entrer des nombres valides.\n")
        except ZeroDivisionError:
            print("-> Erreur : Division par zéro impossible.\n")
        except Exception as e:
            print(f"-> Erreur : {e}\n")

if __name__ == "__main__":
    main()
