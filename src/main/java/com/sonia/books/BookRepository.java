package com.sonia.books;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface BookRepository extends MongoRepository<Book, ObjectId> {
    Optional<Book> findBookByTitle(String title);
}
