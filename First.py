# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)
# print(squares)
# squares = [value ** 2 for value in range(1,11)]
# print(squares)

# age = 23
# # if age < 4:
# #     price = 5
# # elif age < 18:
# #     price = 10
# # else:
# #     price = 20
# # print(price)
# point = 0
# alien_color = ['green','yellow','red']
# killed_alien = 'green'
# alien_0 = {'color':'grenn','point':5}
# print(alien_0['color'])
# alien_0['point'] = 10
# # print(alien_0['point'])
# # aliens = []
# # for alien in range(30):
# #     new_alien = {'color':'green','point':'5','speed':'slow'}
# #     aliens.append(new_alien)
# # print(aliens)
# # for alien in aliens[0:3]:
# #     if alien['color'] == 'green':
# #         alien['color'] = 'yellow'
# #         alien['speed'] = 'medium'
# #         alien['poingt'] = 10
# # for alien in aliens[0:5]:
# #     print(alien)
# pizza = {
#     'crust':'thick',
#     'toppings':['mushrooms','extra cheese'],
# }
# print(pizza['crust'])
# for n in range(2,10):
#     for x in range(2,n):
#         if n % x == 0:
#             print(n,'equals',x,'*',n//x)
#             break
#         else:
#             print(n,'The number is prime')
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i,a[i])
# def fib(n):
# #     result = []
# #     a,b = 0,1
# #     while a<n:
# #         result.append(a)
# #         a,b = b,a+b
# #     print(result)
# #     return result
# # fb1 = fib(100)
# # fb1
def ask_ok(prompt,retries=4,reminder='Please try again!'):
    while True:
        ok=input(prompt)
        if ok in('y','ye','yes'):
            return True
        if ok in('n','no','nop','nope'):
            return  False
        reminder -= 1
        if reminder < 0:
            raise ValueError('invalid user response')
        print(reminder)