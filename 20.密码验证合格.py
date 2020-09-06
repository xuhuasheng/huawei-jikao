# 题目描述
# 密码要求:

# 1.长度超过8位
# 2.包括大小写字母.数字.其它符号,以上四种至少三种
# 3.不能有相同长度大于2的子串重复

# 输入描述:
# 一组或多组长度超过2的子符串。每组占一行

# 输出描述:
# 如果符合要求输出：OK，否则输出NG

# 示例1
# 输入
# 021Abc9000
# 021Abc9Abc1
# 021ABC9000
# 021$bc9000
# 输出
# OK
# NG
# NG
# OK


# 1）生成一个长度为3的所有子串序列（因为长度大于4的相同子串，必定存在长度3的相同子串)；
# 2）if len(set(sub)) < len(sub):return False python 用set去重，判断长度就可以知道是否有重复；
# 3）类型用正则匹配，如果匹配到目标数据格式 type_ += 1；
# 4）最后return True if type_ >= 3 else False；
# 5）处理多行输入输出，调用该函数即可。
def checkLegal(pswd):   
    if len(pswd) <= 8:return False       
    else:
        #最大重复子串长度2+
        sub = []
        for i in range(len(pswd)-2):
            sub.append(pswd[i:i+3])
        if len(set(sub)) < len(sub):return False
        #check type
        type_ = 0
        import re
        Upper = '[A-Z]'
        Lowwer = '[a-z]'
        num = '\d'
        chars = '[^A-Za-z0-9_]'
        patterns = [Upper, Lowwer, num, chars]
        for pattern in patterns:
            pw = re.search(pattern, pswd)
            if pw : type_ += 1
        return True if type_ >= 3 else False
while True:
    try:
        pswd = input()
        print('OK' if checkLegal(pswd) else 'NG')
    except:
        break