class Convertor:
    def __init__(self):
        
        self.val_to_roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def convert(self, num):
       
        

        roman_num = ''
        for value, symbol in self.val_to_roman:
            while num >= value:
                roman_num += symbol
                num -= value
        return roman_num


converter = Convertor()
input_num = int(input('Enter an integer between 1 and 3999: '))
roman_numeral = converter.convert(input_num)
print(f"{input_num} is {roman_numeral}")