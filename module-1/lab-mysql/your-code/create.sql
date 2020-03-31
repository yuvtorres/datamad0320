
USE lab_mysql;

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lab_mysql` DEFAULT CHARACTER SET utf8 ;
USE `lab_mysql` ;

-- -----------------------------------------------------
-- Table `lab_mysql`.`Car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Car` (
  `idCar` INT NOT NULL AUTO_INCREMENT,
  `VIN` INT NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Year` INT NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCar`),
  UNIQUE INDEX `VIN_UNIQUE` (`VIN` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Customer` (
  `idCustomer` INT NOT NULL AUTO_INCREMENT,
  `Customer ID` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL COMMENT '	\n',
  `Phone_number` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `State/Province` VARCHAR(45) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `zip_code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCustomer`),
  UNIQUE INDEX `Customer ID_UNIQUE` (`Customer ID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Salesperson` (
  `idSalesperson` INT NOT NULL AUTO_INCREMENT,
  `Staff ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Store` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSalesperson`, `Staff ID`),
  UNIQUE INDEX `Staff ID_UNIQUE` (`Staff ID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Invoice` (
  `idInvoice` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `Staff ID` INT NOT NULL,
  `Customer ID` VARCHAR(45) NOT NULL,
  `VIN` INT NOT NULL,
  PRIMARY KEY (`idInvoice`, `Customer ID`, `VIN`),
  UNIQUE INDEX `idInvoice_UNIQUE` (`idInvoice` ASC),
  INDEX `fk_Invoice_Salesperson1_idx` (`Staff ID` ASC),
  INDEX `fk_Invoice_Customer1_idx` (`Customer ID` ASC),
  INDEX `fk_Invoice_Car1_idx` (`VIN` ASC),
  CONSTRAINT `fk_Invoice_Salesperson1`
    FOREIGN KEY (`Staff ID`)
    REFERENCES `lab_mysql`.`Salesperson` (`Staff ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoice_Customer1`
    FOREIGN KEY (`Customer ID`)
    REFERENCES `lab_mysql`.`Customer` (`idCustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoice_Car1`
    FOREIGN KEY (`VIN`)
    REFERENCES `lab_mysql`.`Car` (`idCar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

