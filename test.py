def diem(cpa):
    return f'{cpa:.2f}'

def get_gpa(a):
    if a > 0: return 'ok'
a = float(input())
print(diem(a))
print(type(diem(a)))
