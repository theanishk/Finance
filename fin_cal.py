import streamlit as st

st.set_page_config(page_title="Finance Calculators",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# A Financial Calculator. This is application was developed by Anish "
    })

class calculator:
    def inflation(self):
        current_cost = st.number_input('Current Cost', min_value = 0e0, max_value = 1e7, step = 1e1)
        curreny_inflation = st.number_input('Inflation Rate (p.a.)', min_value = 0e0, max_value = 100e0, step = 1e0)
        time = st.number_input('Time Period', min_value = 1, max_value = 50)
        future_cost = current_cost*(1 + curreny_inflation/100)**time
        st.write(f'Current Cost  **:red[{current_cost:.2f}]**')
        st.write(f'Cost Increased  **:red[{future_cost - current_cost:.2f}]**')
        st.write(f'Future Cost  **:red[{future_cost:.2f}]**')

    def ci(self):
        principal_amt = st.number_input('Current Cost', min_value = 0e0, max_value = 1e7, step = 1e1)
        interest = st.number_input('Rate of Interest (p.a.)', min_value = 0e0, max_value = 100e0, step = 1e0)
        time = st.number_input('Time Period', min_value = 1, max_value = 50)
        frequency = st.radio(label = 'Compounding Frequency', options=('Quaterly', 'Half yearly', 'Yearly'))
        if (frequency == 'Quaterly'):
            time *= 4; interest /= 4
        elif (frequency == 'Half yearly'):
            time *= 2; interest /= 2
        
        total_amt = principal_amt*(1 + interest/100)**time
        st.write(f'Principal Amount  **:red[{principal_amt:.2f}]**')
        st.write(f'Total Interest  **:red[{total_amt - principal_amt:.2f}]**')
        st.write(f'Total Amount  **:red[{total_amt:.2f}]**')
    
    def si(self):
        principal_amt = st.number_input('Current Cost', min_value = 0e0, max_value = 1e7, step = 1e1)
        interest = st.number_input('Rate of Interest (p.a.)', min_value = 0e0, max_value = 100e0, step = 1e0)
        time = st.number_input('Time Period', min_value = 1, max_value = 50)
        total_intrst = principal_amt*interest*time/100
        st.write(f'Principal Amount  **:red[{principal_amt:.2f}]**')
        st.write(f'Total Interest  **:red[{total_intrst:.2f}]**')
        st.write(f'Total Amount  **:red[{total_intrst + principal_amt:.2f}]**')

    def sip(self):
        monthly_invst = st.number_input('Monthly Investment', min_value = 0e0, max_value = 1e7, step = 1e1)
        return_rate = st.number_input('Expected Return Rate (p.a.)', min_value = 0.01, max_value = 100e0, step = 1e0)
        time = st.number_input('Time Period', min_value = 1, max_value = 50)
        amt_invested = monthly_invst*time*12
        periodic_int = return_rate/1200
        total_val = monthly_invst*((1+periodic_int)/periodic_int)*(((1+periodic_int)**(12*time))-1)
        st.write(f'Invested Amount  **:red[{amt_invested:.2f}]**')
        st.write(f'Est. Returns  **:red[{total_val-amt_invested:.2f}]**')
        st.write(f'Total Value  **:red[{total_val:.2f}]**')
    
    def lumpsum(self):
        total_invst = st.number_input('Total Investment', min_value = 0e0, max_value = 1e7, step = 1e1)
        return_rate = st.number_input('Expected Return Rate (p.a.)', min_value = 0.01, max_value = 100e0, step = 1e0)
        time = st.number_input('Time Period', min_value = 1, max_value = 50)
        total_val = total_invst*(1 + return_rate/100)**time
        st.write(f'Invested Amount  **:red[{total_invst:.2f}]**')
        st.write(f'Est. Returns  **:red[{total_val - total_invst:.2f}]**')
        st.write(f'Total Value  **:red[{total_val:.2f}]**')
    
    def swp(self):
        total_invst = st.number_input('Total Investment', min_value = 0e0, max_value = 1e7, step = 1e1)
        withdraw = st.number_input('Withdrawal per Month', min_value = 0e0, max_value = 5e4, step = 1e1)
        return_rate = st.number_input('Expected Return Rate (p.a.)', min_value = 0.01, max_value = 100e0, step = 1e0)
        time = st.number_input('Time Period', min_value = 1, max_value = 50)
        periodic_int = return_rate/1200
        withdrawn = withdraw*((1+periodic_int)/periodic_int)*(((1+periodic_int)**(12*time))-1)
        remain = total_invst*((1+periodic_int)**(time*12)) - withdrawn
        st.write(f'Invested Amount  **:red[{total_invst:.2f}]**')
        st.write(f'Total Withdrawal  **:red[{withdraw*12*time:.2f}]**')
        st.write(f'Remaining Amount  **:red[{remain:.2f}]**')
    
    def ppf(self):
        yr_invst = st.number_input('Yearly Investment', min_value = 0e0, max_value = 1e7, step = 1e1)
        # periodic_int = st.number_input('Rate of Interest (p.a.)', min_value = 0.01, max_value = 100e0, step = 1e0)
        periodic_int = 7.1/100
        st.write("Rate of Interest (p.a.) : 7.1")
        time = st.number_input('Time Period', min_value = 1, max_value = 50)
        total_val = yr_invst*((1+periodic_int)/periodic_int)*(((1+periodic_int)**time)-1)
        total_invst = yr_invst*time
        st.write(f'Invested Amount  **:red[{total_invst:.2f}]**')
        st.write(f'Total Interest  **:red[{total_val-total_invst:.2f}]**')
        st.write(f'Maturity Value  **:red[{total_val:.2f}]**')

    def nps(self):
        monthly_invst = st.number_input('Monthly Investment', min_value = 0e0, max_value = 1e7, step = 1e1)
        return_rate = st.number_input('Expected Return Rate (p.a.)', min_value = 0.01, max_value = 100e0, step = 1e0)
        age = st.number_input('Your Age', min_value = 18, max_value = 60)
        time = 60-age
        amt_invested = monthly_invst*time*12
        periodic_int = return_rate/1200
        total_val = monthly_invst*((1+periodic_int)/periodic_int)*(((1+periodic_int)**(12*time))-1)
        st.write(f'Invested Amount  **:red[{amt_invested:.2f}]**')
        st.write(f'Est. Returns  **:red[{total_val-amt_invested:.2f}]**')
        st.write(f'Total Value  **:red[{total_val:.2f}]**')


    def emi(self):
        loan_amt = st.number_input('Loan Amount', min_value = 0e0, max_value = 1e7, step = 1e1)
        periodic_int = st.number_input('Rate of Interest (p.a.)', min_value = 0.01, max_value = 100e0, step = 1e0)
        time = st.number_input('Loan Tenure', min_value = 1, max_value = 50)
        mon_int = periodic_int/1200
        time_mon = time*12
        mon_emi = loan_amt*mon_int*((1+mon_int)**(time_mon))/(((1+mon_int)**(time_mon))-1)
        total_amt = mon_emi*time_mon
        st.write(f'Monthly EMI  **:red[{mon_emi:.2f}]**')
        st.write(f'Total Interest  **:red[{total_amt-loan_amt:.2f}]**')
        st.write(f'Total Amount  **:red[{total_amt:.2f}]**')

    def nsc(self):
        total_invst = st.number_input('Total Investment', min_value = 0e0, max_value = 1e7, step = 1e1)
        intrst_rate = st.number_input('Interest Rate (p.a.)', min_value = 0.01, max_value = 100e0, step = 1e0)
        time = st.number_input('Time Period', min_value = 1, max_value = 50)
        frequency = st.radio(label = 'Compounding Frequency', options=('Half yearly', 'Yearly'))
        if (frequency == 'Half yearly'):
            time *= 2; intrst_rate /= 2
        total_val = total_invst*(1 + intrst_rate/100)**time
        st.write(f'Invested Amount  **:red[{total_invst:.2f}]**')
        st.write(f'Total Interest  **:red[{total_val - total_invst:.2f}]**')
        st.write(f'Total Amount  **:red[{total_val:.2f}]**')

st.write('# Finance Calculators')

cal = st.selectbox('Select the calculator',
    ('Inflation', 'Compound Interest', 'Simple Interest', 'SIP', 'Lumpsum',
    'Systematic Withdrawal Plan (SWP)', 'Public Provident fund (PPF)',
     'National Pension System (NPS)', 'EMI', 'National Savings Certificate (NSC) '))

obj = calculator()

if(cal == 'Inflation'):
    obj.inflation()

elif(cal == 'Compound Interest'):
    obj.ci()

elif(cal == 'Simple Interest'):
    obj.si()

elif(cal == 'SIP'):
    obj.sip()

elif(cal == 'Lumpsum'):
    obj.lumpsum()

elif(cal == 'Systematic Withdrawal Plan (SWP)'):
    obj.swp()

elif(cal == 'Public Provident fund (PPF)'):
    obj.ppf()

elif(cal == 'National Pension System (NPS)'):
    obj.nps()

elif(cal == 'EMI'):
    obj.emi()

elif(cal == 'National Savings Certificate (NSC) '):
    obj.nsc()