CREATE TABLE data_type (

  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(45),
  summary VARCHAR(512),
  description TEXT
);

  INSERT INTO data_type (
    name,
    summary,
    description
  ) VALUES (
    "float",
    "Floating point values",
    "a data type that allows us to store multipe values after decimal point"

  );
  INSERT INTO data_type (
    name,
    summary,
    description

  ) VALUES (
    "integers",
    "integer values",
    "data type that store integer values"
  );
  INSERT INTO data_type (
    name,
    summary,
    description
  ) VALUES (
    "booleans",
    "true or false",
    "named after George boole. These can take true or false values."

    
  );
  INSERT INTO data_type (
    name,
    summary,
    description
  ) VALUES (
    "string",
    "are in strings",
    "data that hold simple strings"
  );
  INSERT INTO data_type (
    name,
    summary,
    descripyion
  ) VALUES (
    "list",
    "store non NULL elements",
    "suport but does not require duplicate element values"
  );
  INSERT INTO data_type (
    name,
    summary,
    description
  ) VALUES (
    "dictionaries",
    "store about database definition",
    "is used to execute queries"
  );
  INSERT INTO data_type (
    name, 
    summary,
    description
  ) VALUES (
    "tuples",
    "one row",
    "attribute name paired with an attribute domain"
  );

