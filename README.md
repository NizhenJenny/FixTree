# FixTree
FixTree is an approach to construct tree structures for diff code of a software bug.
# Supported languages
This version supports Java. But more languages are coming soon.
# Related work
It uses the diff tool Gumtree(https://github.com/GumTreeDiff/gumtree) to parse the ASTs of the source code before and after modification respectively.

Its encoding method is based on the encoding approach of TBCNN(https://sites.google.com/site/treebasedcnn/). We have modified and expanded directly on the source code of TBCNN.

# How to
To run this code, you should install BLAS, CBLAS and Gumtree, and make sure "gumtree" is available in command shell.

0. Prepare your data into the \data\original_data directory.
1. Run \03-ConstructCandW\main_TBCNN.py to construct fixtrees and construct networks.
2. Run \xy\Shuffle.py to shuffle.
3. Run \04-train\train_TBCNN.py to train and create paramTest.
4. Run sh TBCNN.sh.
5. Run TBCNNtest.

# Visualization
We also provide a way to visualize the fix tree.
