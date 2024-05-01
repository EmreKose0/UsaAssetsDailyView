import psycopg2

def call_insert_assets_list(ticker, volume):
    try:
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )

        # Veritabanı bağlantısı oluştur
        cur = conn.cursor()

        # Saklı prosedürü çağır
        cur.callproc("insert_assets_list", (ticker, volume))

        # Değişiklikleri kaydet
        conn.commit()

        print("Stored procedure successfully executed.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while calling stored procedure:", error)

    finally:
        # Veritabanı bağlantısını kapat
        if conn is not None:
            conn.close()
            cur.close()


def fetch_data_from_table():
    try:
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )

        # Veritabanı bağlantısı oluştur
        cur = conn.cursor()
        assets_codes = []
        # SQL sorgusunu oluştur
        sql_query = "SELECT code FROM your_table_name"  # Tablo adını ve sorguyu uygun şekilde değiştirin

        # Sorguyu çalıştır
        cur.execute(sql_query)

        # Sonuçları al
        rows = cur.fetchall()

        # Verileri işle
        for row in rows:
            assets_codes.append(row)
            print(row)  # Verileri istediğiniz şekilde işleyebilirsiniz

        return assets_codes

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while fetching data from table:", error)

    finally:
        # Veritabanı bağlantısını kapat
        if conn is not None:
            conn.close()
            cur.close()

def call_insert_assets_price_daily(code,date,open,high,low,close, volume):
    try:
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )

        # Veritabanı bağlantısı oluştur
        cur = conn.cursor()

        # Saklı prosedürü çağır
        cur.callproc("insert_assets_price", (code,date,open,high,low,close, volume))

        # Değişiklikleri kaydet
        conn.commit()

        print("Stored procedure successfully executed.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while calling stored procedure:", error)

    finally:
        # Veritabanı bağlantısını kapat
        if conn is not None:
            conn.close()
            cur.close()
