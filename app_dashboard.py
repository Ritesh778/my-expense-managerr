from script import *
import pandas as pd
import plotly.express as px
import streamlit as st

def main(username,name):
        st.title("#")
        st.markdown(f"""
                    <h1>Hey There<span style="color:red"> {name}</span> !</h1>
                    """,unsafe_allow_html=True)
        st.write("")
        st.write("")
        menu = ["Create","Read","Update","Delete"]
        choice=st.sidebar.selectbox("Select required command",menu)
        create_table()

        if choice=="Create":
            date = st.date_input("Date")
            details= st.text_area("Fill The Details")
            remark= st.selectbox("Remark",["Select payment method","NetBanking","Cash","UPI"])
            credit=st.text_input("Enter credited amount")
            debit=st.text_input("Enter the debited amount")
            total=st.text_input("Enter total amount")
            if st.button("Add Details"):
                add_data(username,date,details,remark,credit,debit,total)
                st.success("Added ::{} ::To Record".format(details))

        elif choice=="Read":
            with st.expander("View All"):
                result=view_all_data(username)
                new_df=pd.DataFrame(result,columns=["username","date","details","remark","credit","debit","total"])
                new_df.drop('username',axis=1,inplace=True)
                st.dataframe(new_df)
            with st.expander("Expense Status"):
                date_df=new_df["details"].value_counts().to_frame()
                date_df=date_df.reset_index()
                st.dataframe(date_df)
            
                p1=px.pie(date_df,names='index',values='details')
                st.plotly_chart(p1,use_container_width=True)
    
    
        elif choice=="Update":
            st.subheader("Edit items")
            with st.expander("Current Data"):
                result=view_all_data(username)
                new_df=pd.DataFrame(result,columns=["username","date","details","remark","credit","debit","total"])
                new_df.drop('username',axis=1,inplace=True)
                st.dataframe(new_df)
            
            list_of_dates=[i[0] for i in view_all_dates(username)]
            selected_dates=st.selectbox("Dates",list_of_dates)
            date_result=get_date(username,selected_dates)
            if date_result:
            
                date=date_result[0][1]
                details = date_result[0][2]
                remark = date_result[0][3]
                credit=date_result[0][4]
                debit=date_result[0][5]
                total=date_result[0][6]
            
                new_date=st.date_input("New date")
                new_details=st.text_area("Transaction details")
                new_remark=st.selectbox("Remark",["select an option","NetBanking","Cash","UPI"])
                new_credit=st.text_input("Enter the updated credit value")
                new_debit=st.text_input("Enter the updated debit value")
                new_total=st.text_input("Enter the updated total")
            
            if st.button("Update Details"):
                edit_task_data(new_date,new_details,new_remark,new_credit,new_debit,new_total,username,date,details,remark,credit,debit,total)
                st.success("Updated ::{} ::To {}".format(date,new_date))
            with st.expander("View Updated Data"):
                result = view_all_data(username)
                new_df = pd.DataFrame(result,columns=["username","date","details","remark","credit","debit","total"])
                new_df.drop('username',axis=1,inplace=True)
                st.dataframe(new_df)
    
    
        elif choice == "Delete":
            st.subheader("Delete")
            with st.expander("View Data"):
                    result = view_all_data(username)
                    new_df = pd.DataFrame(result,columns=["username","date","details","remark","credit","debit","total"])
                    new_df.drop('username',axis=1,inplace=True)
                    st.dataframe(new_df)
            kotha_list = [i[0] for i in view_all_dates(username)]
            kotha_details=[j[0] for j in view_all_details(username)]
            delete_by_task_name =  st.selectbox("Select Date",kotha_list)
            delete_by_detail=st.selectbox("Select Detail",kotha_details)
            if st.button("Delete"):
                    delete_data(username,delete_by_task_name,delete_by_detail)
                    if delete_by_task_name!=None:
                        st.warning("Deleted: '{}'".format(delete_by_task_name))
                    else:
                        st.error("There is nothing to delete")
            with st.expander("Updated Data"):
                    result = view_all_data(username)
                    new_df = pd.DataFrame(result,columns=["username","date","details","remark","credit","debit","total"])
                    new_df.drop('username',axis=1,inplace=True)
                    st.dataframe(new_df)
    
		
if __name__ == '__main__':
        main()