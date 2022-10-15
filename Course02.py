"""
Euler Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor 600851475143 ?
"""
import timeit
# def factorielle(n):
#     for i in range(1, n+1):
#         res *= i
#     return res


# setup_code = """
# def is_prime(number):
#     if number == 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     else:
#         return True
# """
# code = '''
# is_prime(102415541241000545014145204455)
# '''

# execution_time = timeit.timeit(setup=setup_code, stmt=code)
# print(execution_time)


# def is_prime(number):
#     if number == 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     else:
#         return True


# n = 600851475143
# res = 0
# for i in range(1, 10000000):
#     if (n % i == 0) and (is_prime(i)):
#         if i > res:
#             res = i
# print(res)

# def sum(n):
#     res = 0
#     for i in n:
#         res += i
#     return res


# print(sum([5, 6]))


# def sum_2(*number):
#     res = 0
#     for i in number:
#         res += i
#     return res


# print(sum_2(5, 6, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7))


def user_info(**user):
    return user


user = user_info(id=1, fname="Shahin", lname="ABDI", age=30)
if user["id"] == 1:
    print(user["fname"])


user2 = user_info(id=2, fname="Siamak", lname="RAZAVI", age=37)
