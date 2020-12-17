'''
3) 리스트(list)
: 다른 언어의 배열과 같은 형을 의미한다.

리스트의 예> aa = [10, 20, 30]
          movies = ["트랜스포머", "국제시장", "명량"]
          bb = [10, 20, "명량", "국제시장"]
          cc = [10, 20, ["명량", "국제시장"]]
          dd = [] 빈 리스트
    ** 리스트 내에는 어떠한 자료형도 포함시킬 수 있다.

[리스트의 인덱싱과 슬라이싱]
'''

aa = [10, 20, 30]

print(aa[0])

print(aa)

print(aa[1] + aa[2])

print(aa[-1]) #인덱스 값이 -인 경우에는 뒤에서 부터 요소를 가리킨다.

bb = [10, 20, 30, ["ab", "cd", "ef"]] # 이중 리스트구조  

print(bb[0])
print(bb[-1])
print(bb[3])


print(bb[-1][1])

cc = [10, 20, ['aa', 'bb', 'cc',["국제시장", "명량"]]] # 삼중 리스트구조

print(cc[2][3][0]) #삼중 리스트구조에서 인덱싱 하기
print(cc[2][3][1])

# [리스트의 슬라이싱]

ab = [1, 10, 100, 1000, 10000]

print(ab[:3])

ab = "110100100010000"
print(ab[:3])

bc = [1,10,100,['aa','bb','cc'],1000,10000]
print(bc[2:5])

print(bc[3][1:])

# 리스트 연산 (+, *:반복)
aa = [10, 20, 30]

bb = [100, 200, 300]

print(aa+bb)

print(aa*2)

# 리스트의 값을 변경하기

print(aa[1])

aa[1] = 100 # 문자열, 튜플의 형의 요소값은 변경할 수 없지만, 리스트의 요소값은 변경할 수 있다.
print(aa)

print(aa[2:])
aa[2:] = ["국제시장", "명량"]
print(aa)

print(aa[1:3])

aa[1:3] = ["백", "천", "만"]

print(aa)
           
aa[4] = ["십만", "백만", "천만"]

print(aa)






