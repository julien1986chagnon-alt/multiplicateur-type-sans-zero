#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for zero-free multiplication system
"""

import sys
sys.path.insert(0, '..')

from calculator import multiply_without_zero, contains_zero, divide_without_zero

def test_basic_operations():
    """Test basic multiplication cases"""
    print("\n=== BASIC OPERATIONS TEST ===")
    
    test_cases = [
        (4, 3, 12),
        (9, 9, 89),
        (27, 5, 148),
        (19, 11, 219),
        (1, 1, 1),
        (5, 2, 11),
    ]
    
    for a, b, expected in test_cases:
        result = multiply_without_zero(a, b)
        status = "✓" if result == expected else "✗"
        print(f"{status} {a} × {b} = {result} (expected {expected})")
        assert result == expected, f"Failed: {a} × {b} = {result}, expected {expected}"

def test_reciprocity():
    """Test that division inverse works perfectly"""
    print("\n=== RECIPROCITY TEST ===")
    
    test_cases = [
        (27, 5),
        (9, 9),
        (19, 11),
        (85, 27),
        (12, 34),
    ]
    
    for a, b in test_cases:
        product = multiply_without_zero(a, b)
        quotient = divide_without_zero(product, b)
        status = "✓" if quotient == a else "✗"
        print(f"{status} ({a} × {b}) ÷ {b} = {quotient} (expected {a})")
        assert quotient == a, f"Failed reciprocity: ({a} × {b}) ÷ {b} = {quotient}, expected {a}"

def test_no_zeros():
    """Verify results contain no zeros"""
    print("\n=== NO ZEROS TEST ===")
    
    test_cases = [
        (4, 3),
        (9, 9),
        (27, 5),
        (81, 81),
        (99, 112),
    ]
    
    for a, b in test_cases:
        result = multiply_without_zero(a, b)
        has_zero = contains_zero(result)
        status = "✓" if not has_zero else "✗"
        print(f"{status} {a} × {b} = {result} (no zero: {not has_zero})")
        assert not has_zero, f"Result contains zero: {result}"

def test_large_numbers():
    """Test with large numbers"""
    print("\n=== LARGE NUMBERS TEST ===")
    
    test_cases = [
        (123456789, 987654321, 135648814827574789),
        (999999999, 999999999, 1234567898765431989),
        (635, 635, 447957),
    ]
    
    for a, b, expected in test_cases:
        result = multiply_without_zero(a, b)
        status = "✓" if result == expected else "✗"
        print(f"{status} {a:,} × {b:,} = {result:,}")
        print(f"   Expected: {expected:,}")
        assert result == expected, f"Failed: {a} × {b} = {result}, expected {expected}"
        
        # Test reciprocity
        quotient = divide_without_zero(result, b)
        assert quotient == a, f"Reciprocity failed: {result} ÷ {b} = {quotient}, expected {a}"
        print(f"   Reciprocity: {result:,} ÷ {b:,} = {a:,} ✓")

def test_commutativity():
    """Test that a × b = b × a"""
    print("\n=== COMMUTATIVITY TEST ===")
    
    test_cases = [
        (27, 5),
        (9, 11),
        (33, 7),
        (12, 34),
    ]
    
    for a, b in test_cases:
        result_ab = multiply_without_zero(a, b)
        result_ba = multiply_without_zero(b, a)
        status = "✓" if result_ab == result_ba else "✗"
        print(f"{status} {a} × {b} = {result_ab}, {b} × {a} = {result_ba}")
        assert result_ab == result_ba, f"Commutativity failed: {a}×{b}={result_ab} ≠ {b}×{a}={result_ba}"

def test_contains_zero():
    """Test zero detection"""
    print("\n=== ZERO DETECTION TEST ===")
    
    test_cases = [
        (123, False),
        (102, True),
        (1000, True),
        (9999, False),
        (10, True),
        (1, False),
    ]
    
    for num, has_zero in test_cases:
        result = contains_zero(num)
        status = "✓" if result == has_zero else "✗"
        print(f"{status} contains_zero({num}) = {result} (expected {has_zero})")
        assert result == has_zero, f"Failed: contains_zero({num}) = {result}, expected {has_zero}"

if __name__ == "__main__":
    print("\n" + "="*50)
    print("MULTIPLICATEUR TYPE SANS ZÉRO - TEST SUITE")
    print("="*50)
    
    try:
        test_contains_zero()
        test_basic_operations()
        test_reciprocity()
        test_no_zeros()
        test_commutativity()
        test_large_numbers()
        
        print("\n" + "="*50)
        print("✅ ALL TESTS PASSED!")
        print("="*50 + "\n")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}\n")
        sys.exit(1)
