# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("beblaylo@calpoly.edu")
print(message)


def smallest(n: float, m: float) -> float:
   if n < m:
      return n  # For which calls below is this statement evaluated?
   else:
      return m


first = smallest(3, 2)  # What is the value of first?
second = smallest(2, 2)  # What is the value of second? Is this a reasonable result? Why or why not?
print(first,second)

def function2(a:int, b:int, c:int):
   if a > b and a > c:
      return a - b
   elif b>c:
      return b + c
   else:
      return 2* c

answer1 = function2(3, 2, 1)
answer2 = function2(2, 3, 1)
answer3 = function2(2, 1, 3)
print(answer1)
print(answer2)
print(answer3)

def checked_access(L:list[int], idx: int):
   test = idx >= 0 and idx < len(L)
   if test:
      return L[idx]
   else:
      return None

first = checked_access([1,0,1], 9)
second = checked_access([1,0,1], 2)
print(first,second)

def length_sum(L : list[str]):
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])
   elif len(L)>1:
      result = len(L[0]) + len(L[1])
   elif len(L) >0:
      result = len(L[0])
   else:
      result = 0
   return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first, second, third)


def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")

print(first, second)