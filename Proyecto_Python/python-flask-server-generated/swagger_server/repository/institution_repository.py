sql_select = "select * from institution where status = 'A'"

class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows
    
    def get_institution_by_id(self,id_institution):
        with self.session_factory() as session:
            rows = session.execute('SELECT * FROM institution WHERE id = :val', {'val': id_institution})
            return rows
    
    def delete_institution_by_id(self,id_institution):
        with self.session_factory() as session:
            rows = session.execute('DELETE FROM institution WHERE id = :val', {'val': id_institution})
            return rows
        
    def add_institution(self,name,description,address,user):
        with self.session_factory() as session:
            rows = session.execute('INSERT INTO institution(name,description,address,created_user) VALUES (%s, %s, %s, %s)',(name, description, address, user))
            return rows

