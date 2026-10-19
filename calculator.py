print("=== My Calculator ===")

a = float(input("पहिलो नम्बर लेख्नुहोस्: "))
op = input("चिन्ह छान्नुहोस् (+, -, *, /): ")
b = float(input("दोस्रो नम्बर लेख्नुहोस्: "))

if op == "+":
    print("उत्तर:", a + b)
elif op == "-":
    print("उत्तर:", a - b)
elif op == "*":
    print("उत्तर:", a * b)
elif op == "/":
    if b != 0:
        print("उत्तर:", a / b)
    else:
        print("शून्यले भाग गर्न मिल्दैन!")
else:
    print("गलत चिन्ह!")
