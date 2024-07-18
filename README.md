# FesdrerRand

这是由 Fesdrer 独立编写的随机数据类型生成器。

能够方便进行信息学奥林匹克竞赛（OI）中的测试数据生成及对拍工作。

接下来依次粗略介绍各个文件的功能（详细功能请看代码）：

# `fesdrerrand.h`

该文件用 c++ 语言编写，是用来辅助编写输入数据生成程序的。其包含 $3$​ 个 `namespace`：`FESDRER_STL`，`FESDRER_RAND`，`FESDRER_CKECK`。

---

`FESDRER_STL` 内包含一个类 `FVector`，这是用平衡树实现的 `vector`，与传统的 `vector` 相比对 `insert()` 和 `erase()` 进行了提速。可以使用的功能有：

- `clear()`， $\mathcal O(1)$
- `assign(int n,int val)`， $\mathcal O(n\log n)$
- `size()`， $\mathcal O(1)$
- `push_back(int val)`， $\mathcal O(\log n)$
- `operator[int index]`， $\mathcal O(\log n)$

以上与函数传统的 `vector` 功能相同。

- `erase(int index)`，删除下标为 $index$ 的元素， $\mathcal O(\log n)$
- `insert(int index,int val)`，在 $index$ 位置前加入元素  $val$， $\mathcal O(\log n)$
- `lower_bound(int val)`，在元素从小到大排序的前提下，求出最小的大于等于 $val$ 的元素的下标， $\mathcal O(\log n)$

这个类主要是为了方便实现下面随机化函数的一些功能的。

---

接下来介绍 `FESDRER_RAND` 核心部分的各种函数（除了 `random()` 和 `randomreal()` 其他的是一个类，用 `.` 调用其中包含的函数）：

- `random()` 这是最基本的随机整数生成器

- `randomreal()` 这是最基本的随机实数生成器

- `RandomBasic` 基本随机函数，包含随机打乱数组、随机生成数组、随机生成字符串

- `RandomPrint` 输出函数，方便地输出数组、图、树

- `RandomAnother` 其他随机函数，包括返回不同地若干数、分离若干数

- `RandomGraphTool` 打乱节点编号、加自环、去重边、生成不连通图等图操作

- `RandomTree`，`RandomGraph`，`RandomHackSpfa`，`RandomDag`，`RandomScc`，`RandomEdcc`，`RandomVdcc` 随机生成各类图，除了 `RandomTree` 和 `RandomHackSpfa` 外都包含 $3$​ 个函数：`check`，`nm` 和一个以图名称命名的函数，分别实现检查点数边数等是否合法、随机生成一组合法点数边数、生成图的功能。

---

`FESDRER_CHECK` 包含 `CheckTree`，`CheckScc`，`CheckEdcc`，`CheckVdcc` 检查树深度、度数、求出极大连通分量。

# `FesdrerIO.py`

该文件用 python 编写，用于方便批量生成测试数据。其中包含一个类 `IOData` 和其他若干函数，具体功能看代码。
