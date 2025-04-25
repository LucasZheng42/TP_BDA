package com.example.BDA_TP3;

import java.util.ArrayList;

import org.springframework.web.bind.annotation.*;


@RestController
public class MyAPI {
	
	public static ArrayList<ClientLocal> ListeClients= new ArrayList<ClientLocal>();
	
	@GetMapping("/HelloWorld")
	public String HelloWorld()
	{
		return "Hello World !";
	}
		
	@GetMapping("/somme{a}+{b}")
	public int somme(@PathVariable int a,@PathVariable int b)
	{
		return a+b;
	}
	@GetMapping("/somme")
	public int sommebis(@RequestParam int a,@RequestParam int b)
	{
		return a+b;
	}
	
	@GetMapping("/getLucas")
	public ClientLocal getLucas()
	{
		return new ClientLocal(1,"Lucas",22);
	}
	static
	{
		ListeClients.add(new ClientLocal("Lucas",2));
		ListeClients.add(new ClientLocal("Daniel",5));
		ListeClients.add(new ClientLocal("Aissa",4));		
	}
	@GetMapping("/getListe")
	public ArrayList<ClientLocal> getListe()
	{
		return ListeClients;
	}
	
	@GetMapping("/getClient{a})")
	public ClientLocal getClient(@PathVariable int a)
	{
		if(a > ListeClients.size())
		{
			return null;
		}
		return ListeClients.get(a);
	}
	
	//On va s'intéresser aux autres opérations qui sont l'ajout, la modification et la suppression des clients de la liste
	
	@PostMapping("/addClient")
	public String addClient(@RequestParam String nom, @RequestParam int age) 
	{
		ClientLocal client = new ClientLocal(nom,age);
		ListeClients.add(client);
		return "Client" + client +"ajouté !";
	}
	
	@PutMapping("/putClient")
	public String addClient(@RequestParam int id,@RequestParam int newage)
	{
		ListeClients.get(id).setAge(newage);
		return "Client" + ListeClients.get(id) +" a été mis à jour !";
	}
	
	@DeleteMapping("/deleteClient")
	public String deleteClient(@RequestParam int id)
	{
		ListeClients.remove(id);
		return "Client id " + id +" supprimé !";
	}
}
