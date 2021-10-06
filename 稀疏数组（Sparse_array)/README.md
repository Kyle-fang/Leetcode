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
- 采用三元组(row, col, data)(或称为ijv format)的形式来存储矩阵中非零元素的信息
- 三个数组 row 、col 和 data 分别保存非零元素的行下标、列下标与值（一般长度相同）
- 故 coo[row[k]][col[k]] = data[k] ，即矩阵的第 row[k] 行、第 col[k] 列的值为 data[k]
![image](https://user-images.githubusercontent.com/47712424/136163211-525a4ff6-48ab-439a-a1d9-1a844f6216ae.png)

#### CSC, compressed sparse column format.

- csc_matrix是按列对矩阵进行压缩的
- 通过 indices, indptr，data 来确定矩阵，可以对比CSR
- data 表示矩阵中的非零数据
- 对于第 i 列而言，该行中非零元素的行索引为indices[indptr[i]:indptr[i+1]]
- 可以将 indptr 理解成利用其自身索引 i 来指向第 i 列元素的列索引
- 根据[indptr[i]:indptr[i+1]]，我就得到了该行中的非零元素个数，如
- 若 index[i] = 1 且 index[i+1] = 1 ，则第 i 列的没有非零元素
- 若 index[j] = 4 且 index[j+1] = 6 ，则第 j列的非零元素的行索引为 indices[4:6]
- 得到了列索引、行索引，相应的数据存放在： data[indptr[i]:indptr[i+1]]

https://user-images.githubusercontent.com/47712424/136164859-1d58bfab-63d0-4984-812a-088f86d72d85.mp4

- 对于矩阵第 0 列，我们需要先得到其非零元素行索引
  - 由 indptr[0] = 0 和 indptr[1] = 1 可知，第 0列行有1个非零元素。
  - 它们的行索引为 indices[0:1] = [0] ，且存放的数据为 data[0] = 8
  - 因此矩阵第 0 行的非零元素 csc[0][0] = 8
- 对于矩阵第 3 列，同样我们需要先计算其非零元素行索引
  - 由 indptr[3] = 4 和 indptr[4] = 6 可知，第 4 行有2个非零元素。
  - 它们的行索引为 indices[4:6] = [4, 6] ，且存放的数据为 data[4] = 1 ，data[5] = 9
  - 因此矩阵第 i 行的非零元素 csr[4][3] = 1 ， csr[6][3] = 9
#### CSR, compressed sparse row format.
- csr_matrix是按行对矩阵进行压缩的
- 通过 indices, indptr，data 来确定矩阵。
- data 表示矩阵中的非零数据
- 对于第 i 行而言，该行中非零元素的列索引为 indices[indptr[i]:indptr[i+1]]
- 可以将 indptr 理解成利用其自身索引 i 来指向第 i 行元素的列索引
- 根据[indptr[i]:indptr[i+1]]，我就得到了该行中的非零元素个数，如
  - 若 index[i] = 3 且 index[i+1] = 3 ，则第 i 行的没有非零元素
  - 若 index[j] = 6 且 index[j+1] = 7 ，则第 j 行的非零元素的列索引为 indices[6:7]
- 得到了行索引、列索引，相应的数据存放在： data[indptr[i]:indptr[i+1]]

https://user-images.githubusercontent.com/47712424/136163760-a6f7a321-47e5-409a-9a72-0600774f74dc.mp4

- 对于矩阵第 0 行，我们需要先得到其非零元素列索引
  - 由 indptr[0] = 0 和 indptr[1] = 2 可知，第 0 行有两个非零元素。
  - 它们的列索引为 indices[0:2] = [0, 2] ，且存放的数据为 data[0] = 8 ， data[1] = 2
  - 因此矩阵第 0 行的非零元素 csr[0][0] = 8 和 csr[0][2] = 2
- 对于矩阵第 4 行，同样我们需要先计算其非零元素列索引
  - 由 indptr[4] = 3 和 indptr[5] = 6 可知，第 4 行有3个非零元素。
  - 它们的列索引为 indices[3:6] = [2, 3，4] ，且存放的数据为 data[3] = 7 ，data[4] = 1 ，data[5] = 2
  - 因此矩阵第 4 行的非零元素 csr[4][2] = 7 ， csr[4][3] = 1 和 csr[4][4] = 2
