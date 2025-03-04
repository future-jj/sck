import re
from collections import defaultdict
import time


def reverse_words(str):
    words = str.split(" ")
    reversed_words = words[::-1]
    return ' '.join(reversed_words);

print(reverse_words("Hello world! Python"))

# 2. 统计文本词频（Top K高频词）
# 题目：输入一段英文文本，统计每个单词的出现次数，返回出现频率最高的前三个单词（忽略大小写，排除标点）。
# 示例：
# 输入："Python is great. Python is easy. Learn Python!"
# 输出：[('python', 3), ('is', 2), ('great', 1)]
# 提示：使用正则表达式分割单词，结合字典统计频率。

def top_three_words(text):
    # 转换为小写并提炼单词
    text_lower = text.lower()
    words = re.findall(r'[a-z]+', text_lower)
    
    # 统计单词频和首次出现的位置
    word_couts = {}
    first_indices = {}
    for idx, word in enumerate(words):
        if word not in word_couts:
            word_couts[word] = 1
            first_indices[word] = idx
        else:
            word_couts[word] += 1

    # 检查字典是否为空
    if not word_couts:
        return []
    # 按单词出现次数降序排列（-item[1]表示取负数实现降序）
    sorted_words = sorted(
        word_couts.items(),
        key=lambda item: (-item[1], first_indices[item[0]])
    )
    
    return sorted_words[:3]

text = "Python is great. Python is easy. Learn Python!"
print(top_three_words(text))


# 3. 字符串压缩（Run-Length Encoding）
# 题目：实现字符串压缩算法，将连续重复字符替换为“字符+次数”。若压缩后字符串未变短，则返回原字符串。
# 示例：
# 输入："aaabbbbcc" → 输出："a3b4c2"
# 输入："abcd" → 输出："abcd"（压缩后长度未变短）
# 提示：遍历字符串并记录连续字符的出现次数。
def compress(s):
    if len(s) <=1 :
        return s
    
    compressed = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
            
            
    compressed.append(f"{current_char}{count}")
    compressed_str = "".join(compressed)
    
    return compressed_str if len(compressed_str) < len(s) else s
    

print(compress("aaabbbbcc"))  # 输出: "a3b4c2"
print(compress("abcd"))       # 输出: "abcd"
print(compress("a"))          # 输出: "a"
print(compress("abbbbbbbbbb"))# 输出: "a1b10"（原长度11，压缩后长度5，返回压缩结果）

# 4. 多层嵌套列表扁平化
# 题目：将任意多层嵌套的列表转换为一维列表。
# 示例：
# 输入：[[1, 2, [3]], 4, [5, [6, 7]]
# 输出：[1, 2, 3, 4, 5, 6, 7]
# 提示：递归检查元素是否为列表。

def flatten(nested_list):
    result = []
    for element in nested_list:
        # 判断某个对象是否为列表类型
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result

input_list = [[1, 2, [3]], 4, [5, [6, 7]]]
print(flatten(input_list))  # 输出: [1, 2, 3, 4, 5, 6, 7]

# 其他测试用例
print(flatten([[1, [2, [3]], 4], 5]))       # 输出: [1, 2, 3, 4, 5]
print(flatten([1, [2, []], 3]))             # 输出: [1, 2, 3]
print(flatten([]))                          # 输出: []
print(flatten([[[[[5]]]]]))                 # 输出: [5]


# 5. 合并两个有序列表并保持排序
# 题目：合并两个已按升序排列的列表，返回一个新列表，且无需使用内置排序函数。
# 示例：
# 输入：[1, 3, 5], [2, 4, 6] → 输出：[1, 2, 3, 4, 5, 6]
# 提示：双指针遍历比较元素大小。

def merge_sorted_lists(list1, list2):
    i = j = 0
    merged = []
    # 双指针遍历比较元素
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list2[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # 输出: [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([2, 4, 6, 8], [1, 3, 5]))  # 输出: [1, 2, 3, 4, 5, 6, 8]
print(merge_sorted_lists([], [1, 2, 3]))  # 输出: [1, 2, 3]

# 6. 矩阵转置（行列互换）
# 题目：使用列表推导式实现矩阵转置。
# 示例：
# 输入：[[1, 2, 3], [4, 5, 6]] → 输出：[[1, 4], [2, 5], [3, 6]]
# 提示：zip(*matrix) 结合列表推导式。

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]



# 测试示例
print(transpose([[1, 2, 3], [4, 5, 6]]))  # 输出: [[1, 4], [2, 5], [3, 6]]
print(transpose([[1], [2], [3]]))        # 输出: [[1, 2, 3]]
print(transpose([]))                     # 输出: []


# 7. 合并多个字典并求和相同键的值
# 题目：合并多个字典，若键重复，则将其对应的值相加。
# 示例：
# 输入：{'a': 1, 'b': 2}, {'b': 3, 'c': 4} → 输出：{'a': 1, 'b': 5, 'c': 4}
# 提示：遍历字典并使用 collections.defaultdict。

# *dicts 允许函数接收任意数量的字典参数。
def merge_dicts(*dicts):
    result = defaultdict(int)  # 自动初始化缺失键的值为0
    for d in dicts:
        for key, value in d.items():
            result[key] += value
    return dict(result)  #转换会普通字典


# 测试示例
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  # 输出: {'a': 1, 'b': 5, 'c': 4}

# 8. 按字典的值排序并返回有序字典
# 题目：将字典按值从大到小排序，返回排序后的新字典。
# 示例：
# 输入：{'apple': 5, 'banana': 2, 'cherry': 8}
# 输出：{'cherry': 8, 'apple': 5, 'banana': 2}
# 提示：使用 sorted() 函数和字典推导式。

def sort_dict_by_value(d):
    return {k: v for k, v in sorted(d.items(), key= lambda x:x[1], reverse=True)}

input_dict = {'apple':5, 'banana':2, 'cherry':8}
out_dict = sort_dict_by_value(input_dict)
print(out_dict)

# 计算嵌套字典中所有数值的总和
# 题目：递归遍历嵌套字典，计算所有整数或浮点数的总和。
# 示例：
# 输入：{'a': 1, 'b': {'c': 2, 'd': [3, {'e': 4}]}} → 输出：10（1+2+3+4）
# 提示：递归处理字典、列表等可迭代对象。

def sum_nested_values(obj):
    total = 0
    if(isinstance(obj, dict)):
        for value in obj.values():
            total += sum_nested_values(value)
    elif isinstance(obj, list):
        for item in obj:
            total += sum_nested_values(item)
    elif isinstance(obj, (int, float)):
        total += obj
    return total

# 示例用法
input_dict = {'a': 1, 'b': {'c': 2, 'd': [3, {'e': 4}]}}
print(sum_nested_values(input_dict))  # 输出：10


def is_strong_password(password):
    if len(password) < 8:
        return False
    
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*]', password) is not None
    
    # 统计满足条件的类型数量
    count = sum([has_upper, has_lower, has_digit, has_special])
    
    return count >= 3


print("Python3!", is_strong_password("Python3!"))       # True（大写、小写、数字、符号）
print("password123", is_strong_password("password123"))     # False（仅小写、数字）
print("Abc123*", is_strong_password("Abc123*"))       # True（大写、小写、数字、符号）
print("Aa1!aaaa", is_strong_password("Aa1!aaaa"))       # True（大写、小写、数字、符号）
print("Short123", is_strong_password("Short123"))      # False（长度不足且类型不足）

# 11. 寻找列表中的众数（出现次数最多的元素）
# 题目：找出列表中出现次数最多的元素（可能有多个）。
# 示例：
# 输入：[1, 2, 2, 3, 3, 3] → 输出：[3]
# 输入：[1, 1, 2, 2] → 输出：[1, 2]
# 提示：结合字典统计和最大值查找。

def find_modes(nums):
    if not nums:
        return []
    counts = {}
    first_occurrence = {}
    for idx, num in enumerate(nums):
        if num not in counts:
            counts[num] = 1
            first_occurrence[num] = idx
        else:
            counts[num] += 1
    max_count = max(counts.values())
    candidates = [num for num, cnt in counts.items() if cnt == max_count]
    candidates.sort(key= lambda x: first_occurrence[x]) 
    return candidates;

# 测试示例
print(find_modes([1, 2, 2, 3, 3, 3]))   # 输出：[3]
print(find_modes([1, 1, 2, 2]))         # 输出：[1, 2]
print(find_modes([2, 2, 1, 1, 3]))      # 输出：[2, 1]
print(find_modes([1, 3, 3, 2, 2, 2]))   # 输出：[2]

# 1. 动态参数处理器（*args 和 kwargs）
# 题目：编写函数 dynamic_processor，接受任意数量的位置参数和关键字参数，返回一个字典：

# 键 "positional"：值是所有位置参数的和（仅处理数值类型参数）

# 键 "keyword"：值是所有关键字参数的值组成的列表（仅处理值为字符串的参数）
# 示例：
# 输入：dynamic_processor(1, 2, 'a', x='hello', y=3, z='world')
# 输出：{'positional': 3, 'keyword': ['hello', 'world']}
# 提示：需过滤非数值类型的位置参数和非字符串类型的关键字参数。

def dynamic_processor(*args, **kwargs):
    sum_pos = 0
    keyword_list = []
    # 处理位置参数，仅累加数值类型
    for arg in args:
        if isinstance(arg, (int, float)):
            sum_pos += arg
            
    # 处理关键字参数: 仅保留值为字符串的参数
    for value in kwargs.values():
        if isinstance(value, str):
            keyword_list.append(value)
    return {'positional':sum_pos, 'keyword':keyword_list}
result = dynamic_processor(1, 100, 'a', x='hello', y='3', z='world')
print(result)  # {'positional': 3, 'keyword': ['hello', 'world']}


# 2. 闭包实现计数器
# 题目：用闭包实现一个计数器函数 create_counter()，每次调用返回的函数时，计数器值自增。支持初始化值和步长：
# create_counter(init=0, step=1)：初始化值和步长
# 示例：
# counter = create_counter(init=5, step=2)
# print(counter())  # 输出 5
# print(counter())  # 输出 7
# print(counter())  # 输出 9

def create_counter(init = 0, step = 1):
    current = init
    def counter():
        nonlocal current
        result = current
        current += step
        return result
    return counter

counter = create_counter(init=5, step=2)

print(counter())  # 输出 5 → current 更新为7
print(counter())  # 输出 7 → current 更新为9
print(counter())  # 输出 9 → current 更新为11

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时{end - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    
slow_function()
        
 

