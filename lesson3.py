{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1d91e69e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* * *\n",
      "* 5 *\n",
      "* * *\n"
     ]
    }
   ],
   "source": [
    "m_list = [\n",
    "    [3,25,6],\n",
    "    [87, 5, 20],\n",
    "    [76, 15, 7]\n",
    "    ]\n",
    "for i in range(len(m_list)):\n",
    "    for j in range(len(m_list[i])):\n",
    "        if i % 2 == 0:\n",
    "            m_list[i][j] = '*'\n",
    "        else:\n",
    "            if j % 2 == 0:\n",
    "                m_list[i][j] = '*'           \n",
    "for i in range(len(m_list)):\n",
    "    print(*m_list[i], sep=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8330fe0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 8 5 9 [0, 1, 2, 6, 10, 56]\n"
     ]
    }
   ],
   "source": [
    "first_list = [1, 2, 56, 3, 8, 5, 9, 0, 2]\n",
    "first_tuple = (3, 6, 10, 8, 9, 5, 3)\n",
    "new_list = []\n",
    "second_list = []\n",
    "new1_list = []\n",
    "\n",
    "for a in first_list:\n",
    "    if a in first_tuple:\n",
    "        print(a, end=' ')\n",
    "        second_list.append(a)\n",
    "    else:\n",
    "        continue\n",
    "\n",
    "first_list.extend(first_tuple)   \n",
    "new_list = set(first_list)\n",
    "\n",
    "for b in new_list:\n",
    "    if b not in second_list:\n",
    "        new1_list.append(b)\n",
    "    else:\n",
    "        continue\n",
    "\n",
    "print(new1_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f82f910",
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
