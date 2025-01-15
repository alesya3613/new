{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "20e4ebb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите переменную: h\n",
      "Введите а: 1\n",
      "Введите b: -2\n",
      "Введите c: -63\n",
      "Данное уравнение имеет 2 корня: \n",
      "h1 = 9.0 \n",
      "h2 = -7.0\n"
     ]
    }
   ],
   "source": [
    "#Задание 1\n",
    "from math import sqrt\n",
    "\n",
    "v = input('Введите переменную: ')\n",
    "a = int(input('Введите а: '))\n",
    "b = int(input('Введите b: '))\n",
    "c = int(input('Введите c: '))\n",
    "\n",
    "def quadratic_equation(a, b, c):\n",
    "    dis = b**2 - 4*a*c\n",
    "    \n",
    "    if dis > 0:\n",
    "        x1 = (-b + sqrt(dis)) / (2*a)\n",
    "        x2 = (-b - sqrt(dis)) / (2*a)\n",
    "        return f'Данное уравнение имеет 2 корня: \\n{v}1 = {x1} \\n{v}2 = {x2}'\n",
    "    elif dis == 0:\n",
    "        x = -b / (2*a)\n",
    "        return f'Данное уравнение имеет один корень: \\n{v} = {x}'\n",
    "    else:\n",
    "        return 'Данное уравнение не имеет корней'\n",
    "        \n",
    "    \n",
    "    \n",
    "print(quadratic_equation(a, b, c))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ac0f096e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Введите переменную: x\n",
      "Введите а: 1\n",
      "Введите b: 4\n",
      "Введите c: -5\n",
      "Корни уровнения: \n",
      "x1 = 3.0 \n",
      "x2 = -3.0 \n",
      "x3 = 1.7320508075688772 \n",
      "x4 = -1.7320508075688772\n"
     ]
    }
   ],
   "source": [
    "#(x^2 - 8)^2 + 4(x^2 - 8) - 5 = 0\n",
    "from math import sqrt\n",
    "\n",
    "v = input('Введите переменную: ')\n",
    "a = int(input('Введите а: '))\n",
    "b = int(input('Введите b: '))\n",
    "c = int(input('Введите c: '))\n",
    "\n",
    "def equation(a, b, c):\n",
    "    dis = b**2 - 4*a*c\n",
    "    \n",
    "    if dis > 0:\n",
    "        t1 = (-b + sqrt(dis)) / (2*a)\n",
    "        t2 = (-b - sqrt(dis)) / (2*a)\n",
    "        \n",
    "        x1 = sqrt(t1 + 8)\n",
    "        x2 = -sqrt(t1 + 8)\n",
    "        x3 = sqrt(t2 + 8)\n",
    "        x4 = -sqrt(t2 + 8)\n",
    "        \n",
    "        return f'Корни уровнения: \\n{v}1 = {x1} \\n{v}2 = {x2} \\n{v}3 = {x3} \\n{v}4 = {x4}'\n",
    "    elif dis == 0:\n",
    "        t = -b / (2*a)\n",
    "        x1 = sqrt(t + 8)\n",
    "        x2 = -sqrt(t + 8)\n",
    "        return f'Корни уровнения: \\n{v}1 = {x1} \\n{v}2 = {x2}'\n",
    "    else:\n",
    "        return 'Данное уравнение не имеет корней'\n",
    "        \n",
    "    \n",
    "    \n",
    "print(equation(a, b, c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d8aa1b20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 4, 3, 2, 1]\n",
      "[5, 4, 3, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "#Задание 2\n",
    "list1 = [1, 2, 3, 4, 5]\n",
    "list2 = []\n",
    "\n",
    "for i in range(len(list1)-1, -1, -1): #способ 1\n",
    "    list2.append(list1[i])\n",
    "print(list2)\n",
    "\n",
    "list3 = list(reversed(list1)) #способ 2\n",
    "print(list3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f8a4e353",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 2, 3, 4, 1]\n"
     ]
    }
   ],
   "source": [
    "#Задание 3\n",
    "lst = [1, 2, 3, 4, 5]\n",
    "\n",
    "def change(lst):\n",
    "    first_num  = lst[0]\n",
    "    lst[0] = lst[len(lst)-1]\n",
    "    lst[len(lst)-1] = first_num\n",
    "    return lst\n",
    "    \n",
    "print(change(lst))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1c1ce5da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10.833333333333334\n"
     ]
    }
   ],
   "source": [
    "#Задание 4\n",
    "s = [54, 65, 17, 1, 34, 10]\n",
    "\n",
    "def useless(s):\n",
    "    num = max(s) / len(s)\n",
    "    return num\n",
    "    \n",
    "print(useless(s))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e7781657",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['крот____', 'белка___', 'выхухоль']\n"
     ]
    }
   ],
   "source": [
    "#Задание 5\n",
    "lst = ['крот', 'белка', 'выхухоль']\n",
    "\n",
    "def all_eq(lst):\n",
    "    m_word = ''\n",
    "    \n",
    "    for i in range(len(lst)):\n",
    "        if len(m_word) < len(lst[i]):\n",
    "            m_word = lst[i] \n",
    "            \n",
    "    for a in range(len(lst)):\n",
    "        if lst[a] != m_word:\n",
    "            lst[a] += '_'*(len(m_word)-len(lst[a]))\n",
    "\n",
    "    return lst\n",
    "    \n",
    "print(all_eq(lst))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5dd32df",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
