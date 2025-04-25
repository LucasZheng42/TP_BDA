package com.example.BDA_TP3.repository;

import org.springframework.data.jpa.repository.*;
import com.example.BDA_TP3.entities.ClientJPA;

public interface ClientJPARepository extends JpaRepository <ClientJPA, Long>
{
	
}
