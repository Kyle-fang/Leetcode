### 稀疏数组定义：
- 在数值分析中，是其元素大部分为零的矩阵。反之，如果大部分元素都非零，则这个矩阵是稠密的。
### 为什么？
- 在使用计算机存储和操作稀疏矩阵时，经常需要修改标准算法以利用矩阵的稀疏结构。由于其自身的稀疏特性，通过压缩可以大大节省稀疏矩阵的内存代价。更为重要的是，由于过大的尺寸，标准的算法经常无法操作这些稀疏矩阵。

### 稀疏矩阵的格式
- 稀疏矩阵的存储格式往往依赖具体问题中稀疏矩阵的特征，因此其格式比较多。其中一部分是相对简单而又普遍使用的。例如下面列出的格式，均广泛使用。这篇文章主要介绍每种存储类型实现的基本想法。

  - COO, coordinate format.
  - CSR, compressed sparse row format.
  - MSR, modified sparse row format.
  - CSC, compressed sparse column format.
  - MSC, modified sparse column format.
  - DIA, the diagonal sparse matrix format (NOT a diagonal matrix!).
  - DIAG, a diagonal matrix, stored as a vector.
  - LNK, linked storage format.
  - BSR, block row sparse format.
  - DOK,Dictionary of keys
  - BND, the LINPACK format for general banded matrices.
  - ELL, ELLPACK/ITPACK, the format used by ELLPACK and ITPACK.
  - HB, Harwell-Boeing format. (Actually, CSR format plus auxilliary data)
  - JAD, the jagged diagonal format.
  - SSK, Symmetric skyline format.
  - SSR, Symmetric sparse row format.
#### COO, coordinate format.
- COO格式是将矩阵中的非零元素以坐标的方式存储。例如下面的矩阵：

- COO格式即将非零元素的行，列，值三个元素记录下来形成下面的表格。

因此可以用两个长为nnz（非零元素的个数）整数数组分别表示行列指标，用一个实数数组表示矩阵元。

#### DOK,Dictionary of keys

DOK的存储格式与COO格式相同，只是用字典变量存数稀疏矩阵的矩阵元。行列值作为字典的键，矩阵元作为字典内容。以上面为例。
![image](https://user-images.githubusercontent.com/47712424/136161780-7b0f0ae1-a825-4564-8733-bc060c6854d4.png)
