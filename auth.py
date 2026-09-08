class auth:
    def create_database(**kwargs):
        coloumn = []

        for name,datatype in kwargs.items():
            if datatype == "table":
                table_making = f"CREATE TABLE IF NOT EXISTS {name}"
            elif datatype == "num":
                coloumn.append(f"{name} INTEGER")
            elif datatype == "text":
                coloumn.append(f"{name} TEXT")
            elif datatype == "unq_num":
                coloumn.append(f"{name} INTEGER UNIQUE")
            elif datatype == "unq_text":
                coloumn.append(f"{name} TEXT UNIQUE")
            else:
                return "only table,num,text,unq_num and unq_text are allowed"

            if coloumn:
                import sqlite3
                if datatype == "name.db":
                    try:
                        conn = sqlite3.connect(name)
                    except:
                        return "Enter valid name eg: database.db"
                else:
                    conn = sqlite3.connect("database.db")

                query = f"""
                    {table_making} ({", ".join(coloumn)})
                """
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
