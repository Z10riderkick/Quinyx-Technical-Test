
## 1. How long did you take to complete the technical test?

    1 hrs and 52 min

## 2. Was it easy or challenging? Which parts of the test was easy, and which was challenging?

    For me, Part 2 was much more easier than the Part 1. It was indeed very challenging to learn a new frame work in 2 hours. 

    - in part 1, the most challenging part is the time management. How to learn and apply the flask framework in the limited time, then trying to optimize the syntax and solution of the task. The time spent on the learning and applying should be balanced and flexible, which can eventually make the result in a high quality. It also remind me not to make the question too complex or chase for the unneccessary perfectection, which could possibilly waste you a lot of time.

    - in part 2, the most challenging part is to find out the solution and validate the result. the caculation of sales and count on the transaction not cost me a lot of time. But the time calculation and format literally became a barrier for a while, until I suddenly realize the time can be transfer to the time stamp, which is in the format of integer that can be calculated directly.   

## 3. What resources did you use to learn how to solve the test (i.e. Google, forums, books)?

    Stack Overflow, Official documentation, and Previous experiences

## 4. Briefly describe the process that you went through to find the solution for the problem.

    - Part 1, I first use the tool like PostMan to check the accessibility and the response from the target endpoint. Then, I find out the endpoint given in the case is no longer working, so I find another endpoint on the internet that can produce a similar result. After that, I simulate the given task in one of the web framework I familiar with, to understand what function I probably use and what solution I should apply. The task requires to make an API call to the target endpoint to retreive the data, and save the data to show it later on the web page of another endpoint. After finishing this, I go through the start-up documentation of Flask, and searching on the blogs or forums for problems that I cannot solve in a short time. At the end, I validate the result and examine the code to avoid potential bug that may happened

    - Part 2, The first thing I do is to examine the data file provided and the given task, which tells me everything I have to find the solution. After the examination, I found the calculation of sales and count on the transaction can be easily done in an iteration style at the same time. In that case, the final problem was to find the solution to group-up the data in a 15-min time bucket. My solution for the problem is to use the time stamp instead of the time to do the calculation and comparison, since the time stamp is in a format of integer number. I use the first line of time to find out the nearest start time of the time bucket, using the floor division in python. Then, use only one iteration to calculate the total sales and numbers of transactions to minimize the processing time.      

## 5. Are there any other key experiences/notes that you would like us to know in regard to your experience in taking the test

    The journey to find out the solution giving me a lot of accompolishment, and I can find myself improving on the way learning a new technology or tools.  
