<?php
    class API {
        // database properties
        private $conn;
        private $users_table = 'users';
        private $posts_table = 'posts';
        private $token = 'GiCe7zHc';

        // constructor
        public function __construct($db) {
            $this->conn = $db;
        }

        // verify token
        public function verify($token) {
            return $token === $this->token ? true : false;
        }

        // login
        public function login($username, $password) {
            $query = 'SELECT * FROM ' . $this->users_table . ' WHERE username = :username';
            $stmt = $this->conn->prepare($query);

            $username = htmlspecialchars(strip_tags($username));
            $password = htmlspecialchars(strip_tags($password));

            $stmt->bindParam(':username', $username);
            $stmt->execute();

            $result = $stmt->fetch(PDO::FETCH_ASSOC);

            if (password_verify($password, $result['password'])) {
                return true;

            } else {
                return false;

            }
            
        }

        // get all posts
        public function read_all() {
            $query = 'SELECT * FROM ' . $this->posts_table . ' ORDER BY date DESC';
            $stmt = $this->conn->prepare($query);
            $stmt->execute();

            return $stmt;
        }

        // get a single post by id
        public function read_single($id) {
            $query = 'SELECT * FROM ' . $this->posts_table . ' WHERE id = ? LIMIT 1';
            $stmt = $this->conn->prepare($query);
            $stmt->bindParam(1, $id);
            $stmt->execute();

            return $stmt;
        }

        // create a new post
        public function create($title, $image, $body) {
            $query = 'INSERT INTO ' . $this->posts_table . ' SET title = :title, slug = :slug, image = :image, body = :body';
            $stmt = $this->conn->prepare($query);

            $title = htmlspecialchars(strip_tags($title));
            $image = htmlspecialchars(strip_tags($image));

            $slug = preg_replace('/\s+/', '-', strtolower($title));

            $stmt->bindParam(':title', $title);
            $stmt->bindParam(':slug', $slug);
            $stmt->bindParam(':image', $image);
            $stmt->bindParam(':body', $body);

            if ($stmt->execute()) {
                return true;
                
            } else {
                printf("Error: %s.\n", $stmt->error);
                return false;

            }
            
        }

        // update an existing post
        public function update($id, $title, $image, $body) {
            $query = 'UPDATE ' . $this->posts_table . ' SET title = :title, slug = :slug, image = :image, body = :body WHERE id = :id';
            $stmt = $this->conn->prepare($query);

            $id = htmlspecialchars(strip_tags($id));
            $title = htmlspecialchars(strip_tags($title));
            $image = htmlspecialchars(strip_tags($image));

            $slug = preg_replace('/\s+/', '-', strtolower($title));

            $stmt->bindParam(':id', $id);
            $stmt->bindParam(':title', $title);
            $stmt->bindParam(':slug', $slug);
            $stmt->bindParam(':image', $image);
            $stmt->bindParam(':body', $body);

            if ($stmt->execute()) {
                return true;
                
            } else {
                printf("Error: %s.\n", $stmt->error);
                return false;
                
            }
            
        }

        // delete an existing post
        public function delete($id) {
            $query = 'DELETE FROM ' . $this->posts_table . ' WHERE id = :id';
            $stmt = $this->conn->prepare($query);

            $id = htmlspecialchars(strip_tags($id));

            $stmt->bindParam(':id', $id);

            if ($stmt->execute()) {
                return true;
                
            } else {
                printf("Error: %s.\n", $stmt->error);
                return false;
                
            }
        }
    }
?>
