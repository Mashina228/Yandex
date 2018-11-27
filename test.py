class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(LengthError):
    pass


class DigitError(LetterError):
    pass


class SequenceError(DigitError):
    pass


class WordError(SequenceError):
    pass


all = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf',
       'dfg', 'fgh', 'ghj', 'hjk', 'jkl', 'zxc', 'xcv', 'cvb',
       'vbn', 'bnm', 'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ',
       'шщз', 'щзх', 'зхъ', 'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж',
       'джэ', 'жэё', 'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю']
data_passwords = open("top 10000 passwd.txt").read().split()
data = set(open("top-9999-words.txt").read().split())
b = set(data_passwords)
vs = {'SequenceError': 0, 'LetterError': 0, 'DigitError': 0, 'WordError': 0, 'LengthError': 0}


class Obrabotka:
    def __init__(self, do):
        self.trying = do

    def le(self):
        if len(self.trying) < 9:
            raise LengthError('LengthError')

    def seq(self):
        if any([n in self.trying.lower() for n in all]):
            raise SequenceError('SequenceError')

    def let(self):
        if (self.trying.islower() or self.trying.isupper() or self.trying.isdigit() or
                not self.trying.isalpha()):
            raise LetterError('LetterError')

    def di(self):
        if not any([n in self.trying for n in set('0123456789')]):
            raise DigitError('DigitError')

    def wo(self):
        if ghr(self.trying) != ' ':
            raise ghr(self.trying)


def main():
    for i in b:
        c = Obrabotka(i)
        try:
            c.le()
        except PasswordError as e:
            vs[e] += 1
        try:
            c.let()
        except PasswordError as e:
            vs[e] += 1
        try:
            c.di()
        except PasswordError as e:
            vs[e] += 1
        try:
            c.seq()
        except PasswordError as e:
            vs[e] += 1
        try:
            c.wo()
        except PasswordError as e:
            vs[e] += 1


def ghr(d):
    for i in data:
        if i in d:
            raise WordError('WordError')
    return ' '


main()
for g in sorted(vs):
    print(g + ' - ' + str(vs[g]))
