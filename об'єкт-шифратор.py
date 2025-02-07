import random

class Encryptor:
    def __init__(self, *numbers):
        self._numbers = numbers  # приховані вхідні числа.
        self._result = self._encrypt()
    
    def _encrypt(self):
        operation = random.choice(['+', '-', '*', '/'])
        result = self._numbers[0]
        for num in self._numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '-':
                result -= num
            elif operation == '*':
                result *= num
            elif operation == '/' and num != 0:
                result /= num
        return result
    
    def __str__(self):
        return f'Encrypted result: {self._result}'

# приклад використання.
encryptor = Encryptor(10, 5, 3)
print(encryptor)
