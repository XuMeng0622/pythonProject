def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def main():
    num1 = 5
    num2 = 3

    # 调用乘法函数并打印结果
    product_result = multiply_numbers(num1, num2)
    print(f"两数相乘的结果为: {product_result}")

    # 调用加法函数并打印结果
    sum_result = add_numbers(num1, num2)
    print(f"两数相加的结果为: {sum_result}")


    # 计算一个复杂的表达式并打印结果
    complex_result = add_numbers(sum_result, product_result) * 2
    print(f"经过复杂计算后的结果为: {complex_result}")

if __name__ == "__main__":
    main()