# Fluent Python
## 把函数视作对象
- [ ] 函数也是对象的, 你可以把函数赋值给变量, 函数作为参数, 也可以把函数作为返回值
- [ ] 实例化的对象也可以作为函数使用, 这时候只需要实现__call__方法即可
- [ ] 写项目代码的时候, 要验证函数的输入和输出, 稳扎稳打, 无误之后再进入下一环节
## 目录文件说明
- [ ] 凡是数字开头的目录都是【fluent python】的书本附带的完整优秀代码
- [ ] practice目录是我自己看这本书和运行相关代码的时候的自我实践
## 心得
- [ ] 看一本书的时候很枯燥, 完全可以把这本书的code git clone下来, 然后run & debug, 有疑惑再去看书, 交相验证
- [ ] python的dis模块的dis函数可以查看譬如函数的bytecode
- [ ] jobs说过, 每天都是最后一天, 成为你自己, 充分挖掘自己的潜力, 时间来不急了hhh
- [ ] itertools关于迭代器和生成器的资料很多很多的
## Python KeyWord (关键词)
- [ ] nonlocal, 它的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量
```
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count+= 1
        total+= new_value
        return total / count
    return averager
``` 
- [ ] ==运算符比较两个对象的值（对象中保存的数据），而is比较对象的标识
## 几种编程范式
- [ ] 面向过程编程 (OPP)
- [ ] 面向对象编程 (OOP)
- [ ] 函数式编程 (FP)
- [ ] 面向AI编程 (AIP)
## QA
- [ ] 【OOP】类方法和静态方法的区别是什么呢?
- [ ] Python写个计算器吧, 以及 中缀运算符?