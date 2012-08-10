#for i in input():print['****\n*  *\n*  *\n*  *\n****',' ** \n  * \n  * \n  * \n ***','****\n*  *\n  * \n *  \n****','****\n   *\n ***\n   *\n****'][int(i)]+'\n'

x=[['****\n*  *\n*  *\n*  *\n****',' ** \n  * \n  * \n  * \n ***','****\n*  *\n  * \n *  \n****','****\n   *\n ***\n   *\n****'][int(i)]for i in input()]
for i in range(5):print' '.join([y.split('\n')[i]for y in x])