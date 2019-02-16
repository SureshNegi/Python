#https://www.programiz.com/python-programming/array
import array as arr
a = arr.array('d', [1, 3, 5])   #error

#search the element in array
def find(arr, n):
    for item in arr:
        if item==n:
            return True;
    return False;

result=find(a,6);
print(result);
        
        
