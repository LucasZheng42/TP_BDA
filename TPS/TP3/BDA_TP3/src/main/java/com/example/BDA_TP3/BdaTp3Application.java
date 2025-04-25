package com.example.BDA_TP3;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.example.BDA_TP3.entities.ClientJPA;
import com.example.BDA_TP3.repository.ClientJPARepository;


@SpringBootApplication
public class BdaTp3Application {

	public static void main(String[] args) {
		SpringApplication.run(BdaTp3Application.class, args);
		
	}
	@Bean
	CommandLineRunner runner(ClientJPARepository repository)
	{
		return args -> 
		{
			repository.save(new ClientJPA(0,"Uno","Lucas",2));
			repository.save(new ClientJPA(1,"Dos","Daniel",5));
			repository.save(new ClientJPA(2,"Tres","Aissa",4));
		};
	}
}
