<?php
    class Database {
        private $host = "mysql4112int.cp.blacknight.com";
        private $dbname = "db1516988_blog";
        private $username = "u1516988_zana";
        private $password = "P#ft9k5MX1";
        private $conn;

        public function connect() {
            $this->conn = null;

            try {
                $this->conn = new PDO('mysql:host=' . $this->host . ';dbname=' . $this->dbname, $this->username, $this->password);
                $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            } catch (PDOException $error) {
                echo 'Connection error: ' . $error->getMessage();

            }

            return $this->conn;

        }

    }
?>
