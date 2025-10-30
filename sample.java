package com.example.laptopstore.test;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import com.example.laptopstore.dto.LaptopDTO;
import com.example.laptopstore.entity.Laptop;
import com.example.laptopstore.exception.ResourceNotFoundException;
import com.example.laptopstore.repo.LaptopRepository;
import com.example.laptopstore.service.impl.LaptopServiceImpl;

// Comprehensive JUnit test suite for LaptopService
@ExtendWith(MockitoExtension.class)
@DisplayName("Laptop Service Test Suite")
public class LaptopServiceTest {

    @Mock
    private LaptopRepository laptopRepository;

    @InjectMocks
    private LaptopServiceImpl laptopService;

    private Laptop testLaptop;
    private LaptopDTO testLaptopDTO;
    private List<Laptop> laptopList;

    @BeforeEach
    public void setUp() {
        testLaptop = new Laptop();
        testLaptop.setId(1L);
        testLaptop.setName("Dell XPS 13");
        testLaptop.setPrice(999.99);
        testLaptop.setBrand("Dell");
        testLaptop.setStorage("512GB SSD");
        testLaptop.setRam("16GB DDR4");
        testLaptop.setProcessor("Intel i7-11th Gen");

        testLaptopDTO = new LaptopDTO();
        testLaptopDTO.setId(1L);
        testLaptopDTO.setName("Dell XPS 13");
        testLaptopDTO.setPrice(999.99);
        testLaptopDTO.setBrand("Dell");
        testLaptopDTO.setStorage("512GB SSD");
        testLaptopDTO.setRam("16GB DDR4");
        testLaptopDTO.setProcessor("Intel i7-11th Gen");

        laptopList = new ArrayList<>();
        laptopList.add(testLaptop);
    }

    @Nested
    @DisplayName("Test Create Laptop Operations")
    class CreateLaptopTests {

        @Test
        @DisplayName("Should create a new laptop successfully")
        public void testCreateLaptopSuccess() {
            when(laptopRepository.save(any(Laptop.class))).thenReturn(testLaptop);
            LaptopDTO result = laptopService.createLaptop(testLaptopDTO);
            assertNotNull(result, "Laptop should not be null");
            assertEquals(testLaptopDTO.getId(), result.getId(), "IDs should match");
            assertEquals(testLaptopDTO.getName(), result.getName(), "Names should match");
            assertEquals(testLaptopDTO.getPrice(), result.getPrice(), "Prices should match");
            assertEquals(testLaptopDTO.getBrand(), result.getBrand(), "Brands should match");
            verify(laptopRepository, times(1)).save(any(Laptop.class));
        }

        // ... Add other tests for create as per requirements
    }

    @Nested
    @DisplayName("Test Get Laptop Operations")
    class GetLaptopTests {
        @Test
        @DisplayName("Should get laptop by ID successfully")
        public void testGetLaptopByIdSuccess() {
            when(laptopRepository.findById(1L)).thenReturn(Optional.of(testLaptop));
            LaptopDTO result = laptopService.getLaptopById(1L);
            assertNotNull(result, "Laptop should not be null");
            assertEquals(testLaptopDTO.getId(), result.getId());
            verify(laptopRepository, times(1)).findById(1L);
        }

        // ... Add other tests for get as per requirements
    }

    @Nested
    @DisplayName("Test Update Laptop Operations")
    class UpdateLaptopTests {
        @Test
        @DisplayName("Should update laptop successfully")
        public void testUpdateLaptopSuccess() {
            LaptopDTO updateDTO = new LaptopDTO();
            updateDTO.setId(1L);
            updateDTO.setName("Dell XPS 15");
            updateDTO.setPrice(1299.99);
            updateDTO.setBrand("Dell");
            updateDTO.setStorage("1TB SSD");
            updateDTO.setRam("32GB DDR4");
            updateDTO.setProcessor("Intel i9-11th Gen");

            Laptop updatedLaptop = new Laptop();
            updatedLaptop.setId(1L);
            updatedLaptop.setName("Dell XPS 15");
            updatedLaptop.setPrice(1299.99);
            updatedLaptop.setBrand("Dell");
            updatedLaptop.setStorage("1TB SSD");
            updatedLaptop.setRam("32GB DDR4");
            updatedLaptop.setProcessor("Intel i9-11th Gen");

            when(laptopRepository.findById(1L)).thenReturn(Optional.of(testLaptop));
            when(laptopRepository.save(any(Laptop.class))).thenReturn(updatedLaptop);

            LaptopDTO result = laptopService.updateLaptop(1L, updateDTO);

            assertNotNull(result);
            assertEquals("Dell XPS 15", result.getName());
            assertEquals(1299.99, result.getPrice());
            verify(laptopRepository, times(1)).findById(1L);
            verify(laptopRepository, times(1)).save(any(Laptop.class));
        }
        // ... Add other tests for update as per requirements
    }

    @Nested
    @DisplayName("Test Delete Laptop Operations")
    class DeleteLaptopTests {
        @Test
        @DisplayName("Should delete laptop successfully")
        public void testDeleteLaptopSuccess() {
            when(laptopRepository.existsById(1L)).thenReturn(true);
            doNothing().when(laptopRepository).deleteById(1L);
            boolean result = laptopService.deleteLaptop(1L);
            assertTrue(result, "Delete should return true");
            verify(laptopRepository, times(1)).existsById(1L);
            verify(laptopRepository, times(1)).deleteById(1L);
        }
        // ... Add other tests for delete as per requirements
    }

    @Nested
    @DisplayName("Test Search Laptop Operations")
    class SearchLaptopTests {
        @Test
        @DisplayName("Should search laptop by name successfully")
        public void testSearchLaptopsByNameSuccess() {
            when(laptopRepository.findByName("Dell XPS 13")).thenReturn(laptopList);
            List<LaptopDTO> result = laptopService.searchLaptopsByName("Dell XPS 13");
            assertNotNull(result);
            assertEquals(1, result.size());
            assertEquals("Dell XPS 13", result.get(0).getName());
            verify(laptopRepository, times(1)).findByName("Dell XPS 13");
        }
        // ... Add other tests for search as per requirements
    }

    // ... Continue with edge cases, validation, and repository interaction as outlined above

}