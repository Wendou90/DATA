from app.database import get_db
def output_formatter(results):
    out = []
    for result in results:
      entry = {
        "id": result[0],
        "name": result[1],
        "summary": result[2],
        "description": result[3]
      }
      out.append(entry)
    return out

def scan():
    statement = "SELECT * FROM data_type"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, {})
    out = cursor.fetchall()
    cursor.close()
    return output_formatter(out)

def select_by_type(name="Integers"):
    statement = "SELECT * FROM data_type WHERE name=?"
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(statement, (name, ))
    out = cursor.fetchall()
    cursor.close()
    return output_formatter(out)

def create(raw_json):
    statement = """
        INSERT INTO data_type (
            name,
            summary,
            description

        ) VALUES (?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement,
                  (
                    raw_json["name"],
                    raw_json["summary"],
                    raw_json["description"]
                  )  
            )

    cursor.commit()
    cursor.close()

def update(raw_json, pk): 
    statement = """
         UPDATE data_type
         SET name=?,
         SET summary=?,
         SET description=?
         WHERE id=?
    """ 

    conn = get_db() 
    conn.execute(statement,
        (
            raw_json["name"],
            raw_json["summary"],
            raw_json["description"],
            pk
        )
    
      )
    conn.commit()
    conn.close()


def delete(pk):
    statement = "DELETE FROM data_type WHERE id=?"
    conn = get_db()
    conn.execute(statement, (pk, ))
    conn.commit()
    conn.close()

