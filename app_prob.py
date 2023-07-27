import streamlit as st
from random import randint #데이터프레임으로 표현하는 라이브러리
import pandas as pd

st.title('주사위로 보는 수학적 확률')
trial = st.button('주사위 굴리기')
state = st.session_state.get('dice',[0,0,0,0,0,0])

if trial:
    num = randint(1,6)
    st.write(num)
    state[num-1] = state[num-1]+1
    #state[num-1] += 1
    print(state)
    st.session_state.dice=state


prob = []
print(sum(state))
for i in state:
    prob.append(i/sum(state))
print(prob)

index = [1,2,3,4,5,6]
table = pd.DataFrame({"횟수": state, "확률값": prob}, index=index)

print(table)
st.subheader("시행 결과")
st.dataframe(table)



