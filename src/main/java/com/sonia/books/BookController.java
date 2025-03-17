package com.sonia.books;

import org.bson.types.ObjectId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(maxAge = 3600)
@RestController
@RequestMapping("/api/v1/books")

public class BookController {

    @Autowired
    private BookService bookService;
    @CrossOrigin(origins = "http://localhost:3000")
    @GetMapping
    public ResponseEntity<List<Book>> getAllBooks(){
        return new ResponseEntity<List<Book>>(bookService.allBooks(), HttpStatus.OK);
    }
    @GetMapping("/{title}")
    public ResponseEntity<Optional<Book>> getSingleBook(@PathVariable String title){
        return new ResponseEntity<Optional<Book>>(bookService.singleBook(title), HttpStatus.OK);
    }

}
