package com.example.BDA_TP3.entities;

import jakarta.persistence.*;

@Entity
@Table(name = "client")
public class ClientJPA 
{
	
	@Id
	private int id;
	private String idclient;
	private String prenomclient;
	private int nbrplacesreserveescleint;
	
	public String getIdclient() {
		return idclient;
	}
	public void setIdclient(String idclient) {
		this.idclient = idclient;
	}
	public String getPrenomclient() {
		return prenomclient;
	}
	public void setPrenomclient(String prenomclient) {
		this.prenomclient = prenomclient;
	}
	public int getNbrplacesreserveescleint() {
		return nbrplacesreserveescleint;
	}
	public void setNbrplacesreserveescleint(int nbrplacesreserveescleint) {
		this.nbrplacesreserveescleint = nbrplacesreserveescleint;
	}
	public ClientJPA() {
	
	}

	public ClientJPA(int id, String idclient, String prenomclient, int nbrplacesreserveescleint) {
		super();
		this.id = id;
		this.idclient = idclient;
		this.prenomclient = prenomclient;
		this.nbrplacesreserveescleint = nbrplacesreserveescleint;
	}
	
}
