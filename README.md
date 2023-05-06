# Evaluation of FastCDC: The Effects of Chunk Sizes on Deduplication and Throughput
## Miguel Alonso & Matthew Donlon

Data deduplication is a technique used in storage systems
to reduce data redundancy. It has been widely used by large
storage cloud providers due to the drastic increase in digital
data. It works by identifying and removing duplicate data
blocks, leaving only unique data to be stored. Each block
is identified by a cryptographically secure hash signature,
which is used to identify identical blocks. This can be
achieved at two granularities, at the file or chunk level, each
indicating the size of the block it will be considering. The
main difference between these two approaches is flexibility
and performance overhead. When considering larger blocks,
this will then induce better performance due to the reduced
number of comparisons. On the other hand, variable size
chunking considers different-sized chunks, which will inherently identify more chunks to be deduplicated but will have
a much larger performance overhead.

This project cannot be fully replicated due to the large amount of data we used and couldn't upload. We have uploaded what we could.

### Steps to Recreate

Pull Repo

Install all Dependancies (fastcdc https://github.com/iscc/fastcdc-py)

Change Base Path to personal workspace

Edit plot_folders to remove folders that you dont have (images and compressed images/videos). Many files were to large to upload to github such as the compressed files and memory dumps

#### Memory Dumps

Copy C Memory Dumps into data/memorydumps/initial/C and delete the temp.txt file

Copy Java Memory Dumps into data/memorydumps/initial/Java and delete the temp.txt file


## Running

Jupyter Notebook

Run Block by Block. You may need to edit number of folders being evaluated if they dont exist.
