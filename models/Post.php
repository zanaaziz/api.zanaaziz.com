<?php
    class Post {
        // database properties
        private $conn;
        private $table = 'posts';

        // constructor
        public function __construct($db) {
            $this->conn = $db;
        }

        // get all posts
        public function all() {
            $query = 'SELECT * FROM ' . $this->table . ' ORDER BY date DESC';
            $stmt = $this->conn->prepare($query);
            $stmt->execute();

            return $stmt;
        }

        // get a single post by id
        public function single($id) {
            $query = 'SELECT * FROM ' . $this->table . ' WHERE id = ? LIMIT 1';
            $stmt = $this->conn->prepare($query);
            $stmt->bindParam(1, $id);
            $stmt->execute();

            return $stmt;
        }
    }
?>
