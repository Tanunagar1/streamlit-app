import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="babujaan@1234",
    database="web_db"

)

mycursor = mydb.cursor()
print("connection establish")


def main():
    st.title("crud operations with mysql!")
    option = st.sidebar.selectbox("Select An Operation", ("Create", "Read", "Update", "delete"))

    if option == 'Create':
        st.subheader("Create a record")
        name = st.text_input("Enter Name")
        email = st.text_input("Enter Email")
        if st.button("Create"):
            sql = "insert into users(name,email) values(%s,%s)"
            val = (name, email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record created successfully!")

    elif option == 'Read':
        st.subheader("read records")
        mycursor.execute("select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Update":
        st.subheader("update a record!")
        id = st.number_input("Enter Id", min_value=1)
        name = st.text_input("Enter New Name")
        email = st.text_input("Enter New Email!")
        if st.button("update"):
            sql = "update users set name=%s, email=%s where id =%s"
            val = (name, email, id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("record update successfully!")

    elif option == "delete":
        st.subheader("Delete a Record")
        id = st.number_input("Enter Id", min_value=1)
        if st.button("delete"):
            sql = "delete from users where id = %s"
            val = (id,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record deleted")


if __name__ == '__main__':
    main()
