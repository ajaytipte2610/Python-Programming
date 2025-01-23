# Question 1
import numpy as np
Sales=[100,200,300,400,500,600,700]
Sales_array=np.array(Sales)
print(Sales_array)

#Question 2
import numpy as np
store1_prices = np.array([10, 20, 30])
store2_prices = np.array([1, 2, 3])
addition_result = store1_prices + store2_prices
multiplication_result = store1_prices * store2_prices
print("Addition result:", addition_result)
print("Multiplication result:", multiplication_result)

#Question 3
import numpy as np
sales_january = np.array([300, 400])
sales_february = np.array([500, 600])
Answer=np.concatenate((sales_january,sales_february))
print(Answer)

#Question 4
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6])
Reshap=data.reshape(2,3)
print(Reshap)

#Question 5
import numpy as np
scores = np.array([[80, 90], [85, 95]])
reshaped_scores = scores.reshape(-1)
print(reshaped_scores)