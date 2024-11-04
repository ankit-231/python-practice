# UNF: Repeating groups chuttyaune

Employee ( **E_id**, E_name, E_dob, { E_hire_date, D_id, D_name, Salary, Loc_id, Loc_name, job_status }
)

# 1NF

While performing 1NF, we separate the repeating groups into different relations

Employee-1 ( **E_id**, E_name, E_dob, ,
)

Department-1 ( E*hire_date, **D_id**, D_name, Salary, Loc_id, Loc_name, job_status, \_E_id* )

# 2NF

We check for partial functional dependencies and remove any of them if found

D_id -> D_name, Loc_id, Loc_name (Partial Dependency)

E_id -> X

D_id, E_id -> E_hire_date, Salary, job_status (Full Functional Dependency)

Final Tables in 2NF

Employee-2 ( **E_id**, E_name, E_dob )

Department-2 -> (**D_id**, D_name, Loc_id, Loc_name)

Employee-Department-2 (**D_id, E_id**, E_hire_date, Salary, job_status)

# 3NF

Transitive Dependency.

Primary Key -> Non-Key -> Other Attributes
D_id        -> Loc_id  -> Loc_name

Final Tables in 3NF:

Employee-3 ( **E_id**, E_name, E_dob )

Department-3 -> (**D_id**, D_name, *Loc_id*)

Location-3 -> (**Loc_id**, Loc_name )

Employee-Department-3 (**D_id, E_id**, E_hire_date, Salary, job_status)