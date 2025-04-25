package com.example.BDA_TP3;


public class ClientLocal {
	private static int cpt=0;
	private int id;
	private String nom;
	private int age;
	
	public ClientLocal()
	{
		
	}
	public ClientLocal(String nom,int age)
	{
		this.id = cpt;cpt++;
		this.nom = nom;
		this.age = age;
	}
	public ClientLocal(int id,String nom,int age)
	{
		this.id = id;
		this.nom = nom;
		this.age = age;
	}
	public String getNom() {
		return nom;
	}
	public void setNom(String nom) {
		this.nom = nom;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	@Override
	public String toString() {
		return "ClientLocal [id=" + id + ", nom=" + nom + ", age=" + age + "]";
	}

}
