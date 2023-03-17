{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f967b386",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "#from google.colab import files\n",
    "#uploaded_files = files.upload()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "777cf44c",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic_train = pd.read_csv(\"C:/Users/xxmeh/Downloads/train.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "300ec8ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(891, 12)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e87a69de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "eeb6c1f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived  Pclass                                               Name  \\\n",
       "0         0       3                            Braund, Mr. Owen Harris   \n",
       "1         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...   \n",
       "2         1       3                             Heikkinen, Miss. Laina   \n",
       "3         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)   \n",
       "4         0       3                           Allen, Mr. William Henry   \n",
       "\n",
       "      Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked  \n",
       "0    male  22.0      1      0         A/5 21171   7.2500   NaN        S  \n",
       "1  female  38.0      1      0          PC 17599  71.2833   C85        C  \n",
       "2  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3  female  35.0      1      0            113803  53.1000  C123        S  \n",
       "4    male  35.0      0      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del titanic_train[\"PassengerId\"]\n",
    "titanic_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4071a989",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_Pclass = pd.Categorical(titanic_train[\"Pclass\"], ordered=True)\n",
    "new_Pclass = new_Pclass.rename_categories([\"class1\", \"class2\", \"class3\"])\n",
    "titanic_train[\"Pclass\"] = new_Pclass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "51dcd7b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>counts</th>\n",
       "      <th>freqs</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>categories</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>class1</th>\n",
       "      <td>216</td>\n",
       "      <td>0.242424</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>class2</th>\n",
       "      <td>184</td>\n",
       "      <td>0.206510</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>class3</th>\n",
       "      <td>491</td>\n",
       "      <td>0.551066</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            counts     freqs\n",
       "categories                  \n",
       "class1         216  0.242424\n",
       "class2         184  0.206510\n",
       "class3         491  0.551066"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_Pclass.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "b05d8546",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    714.000000\n",
       "mean      29.699118\n",
       "std       14.526497\n",
       "min        0.420000\n",
       "25%       20.125000\n",
       "50%       28.000000\n",
       "75%       38.000000\n",
       "max       80.000000\n",
       "Name: Age, dtype: float64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic_train[\"Age\"].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "97b70bc4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([  5,  17,  19,  26,  28,  29,  31,  32,  36,  42,  45,  46,  47,\n",
       "         48,  55,  64,  65,  76,  77,  82,  87,  95, 101, 107, 109, 121,\n",
       "        126, 128, 140, 154, 158, 159, 166, 168, 176, 180, 181, 185, 186,\n",
       "        196, 198, 201, 214, 223, 229, 235, 240, 241, 250, 256, 260, 264,\n",
       "        270, 274, 277, 284, 295, 298, 300, 301, 303, 304, 306, 324, 330,\n",
       "        334, 335, 347, 351, 354, 358, 359, 364, 367, 368, 375, 384, 388,\n",
       "        409, 410, 411, 413, 415, 420, 425, 428, 431, 444, 451, 454, 457,\n",
       "        459, 464, 466, 468, 470, 475, 481, 485, 490, 495, 497, 502, 507,\n",
       "        511, 517, 522, 524, 527, 531, 533, 538, 547, 552, 557, 560, 563,\n",
       "        564, 568, 573, 578, 584, 589, 593, 596, 598, 601, 602, 611, 612,\n",
       "        613, 629, 633, 639, 643, 648, 650, 653, 656, 667, 669, 674, 680,\n",
       "        692, 697, 709, 711, 718, 727, 732, 738, 739, 740, 760, 766, 768,\n",
       "        773, 776, 778, 783, 790, 792, 793, 815, 825, 826, 828, 832, 837,\n",
       "        839, 846, 849, 859, 863, 868, 878, 888], dtype=int64),)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "missing = np.where(titanic_train[\"Age\"].isnull()==True)\n",
    "missing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "25cc5c37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "177"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(missing[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "feced104",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:title={'center':'Age'}>]], dtype=object)"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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u/LKK7Mzzzxzt9tluH+uuOKK7G1ve1u2Y8cO2e3FqFGjsksvvbTV2OjRo7OLLrooy7I0vvecTrMH27Zti5UrV0ZdXV2r8bq6uli6dGmZVpWmtWvXRlNTU6ss8/l8DBs2TJa7sHHjxoiIOOqooyJCfvtj+/btsWDBgnjttdfijDPOkN0+uuyyy2LUqFFx9tlntxqX3949+eSTUVtbG/37948LLrggnn766YiQ3b649957Y/DgwfGxj30sjj766Bg0aFDcfvvthe0y3Hfbtm2LO+64Iy699NLI5XKy24szzzwz/vu//zueeOKJiIh49NFH4+GHH44PfOADEZHG917ZPrE1BS+99FJs3749qqurW41XV1dHU1NTmVaVpp157SrLdevWlWNJB60sy2LixIlx5plnxsCBAyNCfvviscceizPOOCP++te/xpve9Ka4++67413velfhzVZ2u7dgwYJYuXJlrFixos0233t7dvrpp8e///u/xzve8Y7485//HNdff30MGTIkVq9eLbt98PTTT8ctt9wSEydOjKuuuiqWLVsWX/rSlyKfz8fFF18sw/1wzz33xCuvvBKXXHJJRHjt7s2VV14ZGzdujOOPPz66du0a27dvjxtuuCE+8YlPREQa+Snx+yCXy7W6nWVZmzH2jSz37vLLL4/f//738fDDD7fZJr/de+c73xmrVq2KV155Je68884YO3ZsLFmypLBddrv23HPPxRVXXBGLFy+Oww47bLf7yW/XRo4cWfjvk046Kc4444x429veFvPmzYt/+Id/iAjZ7cmOHTti8ODB0dDQEBERgwYNitWrV8ctt9wSF198cWE/Ge7dnDlzYuTIkVFbW9tqXHa79sMf/jDuuOOOmD9/fpx44omxatWqmDBhQtTW1sbYsWML+x3M+TmdZg969+4dXbt2bXPUff369W3+Zcae7bxagyz37Itf/GLce++98eCDD8Zb3/rWwrj89q579+7x9re/PQYPHhzTpk2Lk08+Of71X/9VdnuxcuXKWL9+fZx66qnRrVu36NatWyxZsiS+/e1vR7du3QoZyW/fHH744XHSSSfFk08+6XtvH/Tp0yfe9a53tRo74YQT4tlnn40I7337at26dXH//ffHZz7zmcKY7Pbsa1/7WkyePDkuuOCCOOmkk+KTn/xkfPnLX45p06ZFRBr5KfF70L179zj11FOjsbGx1XhjY2MMGTKkTKtKU//+/aOmpqZVltu2bYslS5bIMv72L/vLL7887rrrrnjggQeif//+rbbLb/9lWRbNzc2y24uzzjorHnvssVi1alXha/DgwXHhhRfGqlWr4rjjjpPffmhubo4//vGP0adPH997+2Do0KFtLqf7xBNPxLHHHhsR3vv21dy5c+Poo4+OUaNGFcZkt2dbtmyJLl1a1+CuXbsWLjGZRH7l+X3adOy8xOScOXOyP/zhD9mECROyww8/PHvmmWfKvbSDzubNm7NHHnkke+SRR7KIyGbOnJk98sgjhctx3njjjdkRRxyR3XXXXdljjz2WfeITnzioLtVUTl/4wheyI444IvvlL3/Z6nJhW7ZsKewjv92bMmVK9tBDD2Vr167Nfv/732dXXXVV1qVLl2zx4sVZlsluf/3fq9Nkmfz25Ctf+Ur2y1/+Mnv66aez3/zmN9m5556bVVVVFX5GyG7Pli1blnXr1i274YYbsieffDL7j//4j6yysjK74447CvvIcM+2b9+eHXPMMdmVV17ZZpvsdm/s2LHZW97ylsIlJu+6666sd+/e2aRJkwr7HOz5KfH74N/+7d+yY489NuvevXv293//94XL/tHagw8+mEVEm6+xY8dmWfa3yzVdc801WU1NTZbP57P3ve992WOPPVbeRR8kdpVbRGRz584t7CO/3bv00ksLr9G/+7u/y84666xCgc8y2e2vN5Z4+e3ezutGV1RUZLW1tdno0aOz1atXF7bLbu/+67/+Kxs4cGCWz+ez448/PrvttttabZfhni1atCiLiGzNmjVttslu9zZt2pRdccUV2THHHJMddthh2XHHHZdNnTo1a25uLuxzsOeXy7IsK8v/AgAAANrFOfEAAJAYJR4AABKjxAMAQGKUeAAASIwSDwAAiVHiAQAgMUo8AAAkRokHAIDEKPEAAJAYJR4AABKjxAMAQGKUeAAASMz/Aw6q/nZRr0GDAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 900x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "titanic_train.hist(column=\"Age\", figsize=(9,6), bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "436067d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    891.000000\n",
       "mean      29.361582\n",
       "std       13.019697\n",
       "min        0.420000\n",
       "25%       22.000000\n",
       "50%       28.000000\n",
       "75%       35.000000\n",
       "max       80.000000\n",
       "Name: Age, dtype: float64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_Age_var = np.where(titanic_train[\"Age\"].isnull(), 28, titanic_train[\"Age\"])\n",
    "titanic_train[\"Age\"] = new_Age_var\n",
    "titanic_train[\"Age\"].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "1c4fbd1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:title={'center':'Age'}>]], dtype=object)"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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ihUrmo0ZN25c5HK5Zo+TTz652ZjGxsYYP3589OnTJ7p37x7nnHNOvP7668UfDQAAHARaVeLnz58fl19+eTzzzDNRX18f7777btTW1samTZuajfv0pz8dq1evLjwef/zxZvsnTJgQs2bNipkzZ8bChQtj48aNcdZZZ8W2bduKPyIAAOjgOrdm8K9//etmz6dNmxZ9+/aNxYsXx6c+9anC9nw+HxUVFTt9j/Xr18fUqVPjwQcfjDPOOCMiIqZPnx79+/ePefPmxZlnntnaYwAAgINKq0r8e61fvz4iInr16tVs+1NPPRV9+/aNww8/PIYNGxa33npr9O3bNyIiFi9eHE1NTVFbW1sYX1VVFTU1NbFo0aKdlvjGxsZobGwsPG9oaIiIiKampmhqairmEPbajnkO1HwdieyK057yy3fKSjp/WzJoT/mlRnbFkV9x5Nd2sitOqfPb23lzWZa16V/lLMvis5/9bKxbty6efvrpwvaHHnooDjvssBgwYECsWrUqvv3tb8e7774bixcvjnw+HzNmzIiLLrqoWSmPiKitrY3q6uq47777WsxVV1cXN998c4vtM2bMiG7durVl+QAA0O5s3rw5xowZE+vXr48ePXrsclybz8RfccUV8eKLL8bChQubbT///PMLf66pqYkhQ4bEgAED4rHHHovRo0fv8v2yLItcLrfTfddff31MnDix8LyhoSH69+8ftbW1uz24fampqSnq6+tjxIgRUVZWdkDm7ChkV5z2lF9N3ZySzr+srvWX27Wn/FIju+LIrzjyazvZFafU+e244mRP2lTix48fH48++mgsWLAgjjzyyN2OraysjAEDBsTKlSsjIqKioiK2bt0a69atiyOOOKIwbu3atTF06NCdvkc+n498Pt9ie1lZ2QEPtxRzdhSyK057yK9x285/0D5Qijn+9pBfqmRXHPkVR35tJ7vilCq/vZ2zVXenybIsrrjiinj44YfjiSeeiOrq6j2+5q233orXXnstKisrIyJi8ODBUVZWFvX19YUxq1evjmXLlu2yxAMAAH/XqjPxl19+ecyYMSN++ctfRnl5eaxZsyYiInr27Bldu3aNjRs3Rl1dXXz+85+PysrKePnll+OGG26IPn36xOc+97nC2EsuuSSuuuqq6N27d/Tq1SuuvvrqGDRoUOFuNQAAwK61qsTfe++9ERExfPjwZtun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EqPEAwBAYpR4AABIjBIPAACJUeIBACAxSjwAACRGiQcAgMQo8QAAkBglHgAAEqPEAwBAYpR4AABIjBIPAACJUeIBACAxSjwAACRGiQcAgMQo8QAAkBglHgAAEqPEAwBAYpR4AABIjBIPAACJUeIBACAxSjwAACRGiQcAgMQo8QAAkBglHgAAEqPEAwBAYpR4AABIjBIPAACJUeIBACAxSjwAACRGiQcAgMQo8QAAkBglHgAAEqPEAwBAYpR4AABITKtL/IIFC+Lss8+OqqqqyOVy8cgjjzTbP27cuMjlcs0eJ598crMxjY2NMX78+OjTp0907949zjnnnHj99deLOhAAADhYtLrEb9q0KY4//vi4++67dznm05/+dKxevbrwePzxx5vtnzBhQsyaNStmzpwZCxcujI0bN8ZZZ50V27Zta/0RAADAQaZza18wcuTIGDly5G7H5PP5qKio2Om+9evXx9SpU+PBBx+MM844IyIipk+fHv3794958+bFmWee2dolAQDAQaXVJX5vPPXUU9G3b984/PDDY9iwYXHrrbdG3759IyJi8eLF0dTUFLW1tYXxVVVVUVNTE4sWLdppiW9sbIzGxsbC84aGhoiIaGpqiqampv1xCC3smOdAzdeRyK447Sm/fKespPO3JYP2lF9qZFcc+RVHfm0nu+KUOr+9nTeXZVmb/1XO5XIxa9asOPfccwvbHnrooTjssMNiwIABsWrVqvj2t78d7777bixevDjy+XzMmDEjLrroomalPCKitrY2qqur47777msxT11dXdx8880tts+YMSO6devW1uUDAEC7snnz5hgzZkysX78+evTosctx+/xM/Pnnn1/4c01NTQwZMiQGDBgQjz32WIwePXqXr8uyLHK53E73XX/99TFx4sTC84aGhujfv3/U1tbu9uD2paampqivr48RI0ZEWVnZAZmzo5BdcdpTfjV1c0o6/7K61l9u157yS43siiO/4siv7WRXnFLnt+OKkz3ZL5fT/F+VlZUxYMCAWLlyZUREVFRUxNatW2PdunVxxBFHFMatXbs2hg4dutP3yOfzkc/nW2wvKys74OGWYs6OQnbFaQ/5NW7b+Q/aB0oxx98e8kuV7Iojv+LIr+1kV5xS5be3c+73+8S/9dZb8dprr0VlZWVERAwePDjKysqivr6+MGb16tWxbNmyXZZ4AADg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\n",
      "text/plain": [
       "<Figure size 900x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "titanic_train.hist(column=\"Age\", figsize=(9,6), bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b950d091",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
