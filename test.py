import re


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






