class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        st = [] # Будем хранить кортежи (index, temp)
        res = [0] * len(temperatures)
        
        for i, v in enumerate(temperatures):
            # Пока стек не пуст И текущая температура v больше температуры на вершине стека
            while st and v > st[-1][1]:
                indTemp, temp = st.pop() # Достаем "холодный" день
                res[indTemp] = i - indTemp # Записываем разницу дней для ТОГО индекса
            
            # В любом случае добавляем текущий день в стек
            st.append((i, v))

        return res