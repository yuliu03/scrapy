#写入默认内容，用于未查到信息结果
def defaultWrite(outputDir,info):
    f = open(outputDir, 'a+',encoding='utf-8')
    for sql in info:
        f.write(sql +'\n')  # 加\n换行显示

    f.write("end" + '\n')  # 加\n换行显示
    f.close()

# 将字符串写入tmp文本
def myCopy(str):
    tmp = open("C:/Users/admin/Desktop/tmp1.txt", 'a+', encoding='utf-8')
    tmp.write(str)
    tmp.close()
